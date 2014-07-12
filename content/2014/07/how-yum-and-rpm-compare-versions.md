Title: How Yum and RPM Compare Versions
Date: 2014-07-11 23:31
Author: Jason Antman
Category: Miscellaneous
Tags: rpm, yum, puppet, versions
Slug: how-yum-and-rpm-compare-versions
Summary: A description of the algorithms used by Yum and RPM to compare package versions.

I was recently tripped up by a bug in Puppet, [PUP-1244](https://tickets.puppetlabs.com/browse/PUP-1244),
dealing with how it compares package versions. All of Puppet's Package types assumed
[semantic versioning](http://semver.org/), and that's far from the case for RPMs and therefore Yum. This
manifested itself in how Puppet validates package installations - if a version was explicitly specified
and Yum/RPM could install it, puppet would shell out to them and install the package, but then report
a failure in its post-install validation, as the *exact* version string specified isn't present.
For example, many RedHat/CentOS packages (such as those from EPEL) include a release string with the major
version of the distribution they were packged for - i.e. ".el5" or ".el6". If Puppet was instructed to
install package "foo" version "1.2.3", but the actual package in the repositories was "foo-1.2.3-el5",
Puppet would cause the package to be installed, but then report failure.

I cut a [pull request](https://github.com/puppetlabs/puppet/pull/2866) against the Puppet4 branch to
fix these issues, essentially re-implementing yum and rpm's version comparison logic in Ruby. It took
me a few days of research and sorting through source code (and in the process I found that ``yum``, despite
its use in so many distributions, has no unit tests at all) but I finally got it finished. In the process,
I found out exactly how... weird... RPM's version comparison rules are.

### Package Naming and Parsing

RPM package names are made up of five parts; the package name, epoch, version, release, and architecture.
This format is commonly referred to as the acronym NEVRA. The epoch is not always included; it is assumed
to be zero (0) on any packages that lack it explicitly. The format for the whole string is ``n-e:v-r.a``.
For my purposes, I was only really concerned with comparing the EVR portion; Puppet knows about package names
and the bug herein was with what Puppet calls the "version" (EVR in yum/rpm parlance). Parsing is pretty
simple:

* If there is a ``:`` in the string, everything before it is the epoch. If not, the epoch is zero.
* If there is a ``-`` in the *remaining* string, everything before the first ``-`` is the version,
  and everything after it is the release. If there isn't one, the release is considered null/nill/None/whatever.

### How Yum Compares EVR

Once the package string is parsed into its EVR components, yum calls ``rpmUtils.miscutils.compareEVR()``,
which does some data type massaging for the inputs, and then calls out to ``rpm.labelCompare()``
(found in ``rpm.git/python/header-py.c``). ``labelCompare()`` sets each epoch
to "0" if it was null/Nonem, and then uses ``compare_values()`` to compare each EVR portion, which in turn falls through
to a function called ``rpmvercmp()`` (see below). The algorithm for ``labelCompare()`` is as follows:

1. Set each epoch value to 0 if it's null/None.
1. Compare the epoch values using ``compare_values()``. If they're not equal, return that result, else
   move on to the next portion (version). The logic within ``compare_values()`` is that if one is empty/null
   and the other is not, the non-empty one is greater, and that ends the comparison. If neither of
   them is empty/not present, compare them using ``rpmvercmp()`` and follow the same logic; if one
   is "greater" (newer) than the other, that's the end result of the comparison. Otherwise, move
   on to the next component (version).
2. Compare the versions using the same logic.
3. Compare the releases using the same logic.
4. If all of the components are "equal", the packages are the same.

The real magic, obviously, happens in ``rpmvercmp()``, the rpm library function to compare two
versions (or epochs, or releases). That's also where the madness happens.

### How RPM Compares Version Parts

RPM is written in C. Converting all of the buffer and pointer processing for these strings
over to Ruby was quite a pain. That being said, I didn't make this up, this is actually the
algorithm that ``rpmvercmp()`` (``lib/rpmvercmp.c``) uses to compare version "parts"
(epoch, version, release). This function returns 0 if the strings are equal, 1 if ``a`` (the
first string argument) is newer than ``b`` (the second string argument), or -1 if
``a`` is older than ``b``. Also keep in mind that this uses pointers in C, so it works by removing
a sequence of 0 or more characters from the front of each string, comparing them, and then repeating
for the remaining characters in each string until something is unequal, or a string reaches its end.

1. If the strings are binary equal (``a == b``), they're equal, return 0.
2. Loop over the strings, left-to-right.
   1. Trim anything that's not ``[A-Za-z0-9]`` or tilde (``~``) from the front of both strings.
   2. If both strings start with a tilde, discard it and move on to the next character.
   3. If string ``a`` starts with a tilde and string ``b`` does not, return -1 (string ``a`` is older);
      and the inverse if string ``b`` starts with a tilde and string ``a`` does not.
   4. End the loop if either string has reached zero length.
   5. If the first character of ``a`` is a digit, pop the leading chunk of continuous digits from
      each string (which may be '' for ``b`` if only one ``a`` starts with digits). If ``a`` begins
	  with a letter, do the same for leading letters.
   6. If the segement from ``b`` had 0 length, return ` if the segment from ``a`` was numeric, or
      ``b`` if it was alphabetic. The logical result of this is that if ``a`` begins with numbers
	  and ``b`` does not, ``a`` is newer (return 1). If ``a`` begins with letters and ``b`` does not,
	  then ``a`` is older (return -1). If the leading character(s) from ``a`` and ``b`` were both
	  numbers or both letters, continue on.
   7. If the leading segments were both numeric, discard any leading zeros and *whichever one is longer
      wins*. If ``a`` is longer than ``b`` (without leading zeroes), return 1, and vice-versa. If
	  they're of the same length, continue on.
   8. Compare the leading segments with ``strcmp()`` (or ``<=>`` in Ruby). If that returns a non-zero
      value, then return that value. Else continue to the next iteration of the loop.
3. If the loop ended (nothing has been returned yet, either both strings are totally the same or they're
   the same up to the end of one of them, like with "1.2.3" and "1.2.3b"), then the longest wins -
   if what's left of ``a`` is longer than what's left of ``b``, return 1. Vice-versa for if what's
   left of ``b`` is longer than what's left of ``a``. And finally, if what's left of them is the same
   length, return 0.

Well there you have it. Quite convoluted. And full of things like the "~" magic character ("~1" is always
older than "9999zzzz").
