Title: Dumping all Macros from an RPM Spec File
Date: 2012-09-10 10:00
Author: admin
Category: SysAdmin
Tags: packaging, rpm, rpmbuild
Slug: dumping-all-macros-from-an-rpm-spec-file

I've been doing a lot of RPM packaging lately, and on different (and
very old) distros and versions. Sometimes I lose track of all of the
macros used in specfiles (`_bindir _sbindir dist _localstatedir`, etc).
There's no terribly easy way to dump a list of all of the available
macros. There is, however, a bit of a kludge. Insert the following code
in your specfile before the `%prep` or `%setup` lines:

~~~~{.text}
%dump
exit 1
~~~~

The `%dump` macro will dump all defined macros to STDERR. The `exit 1`
will prevent rpmbuild from going on and trying to build the package. If
you want to view the output nicely, you can pipe it through a pager like
less: `rpmbuild -ba filename.spec 2>&1 | less`.

Just make sure to remove those two lines when you want to actually build
the package.</tt>
