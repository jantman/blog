Title: Easily comparing a bunch of files in one directory
Date: 2012-08-10 09:50
Author: admin
Category: Tech HowTos
Tags: compare, diff
Slug: easily-comparing-a-bunch-of-files-in-one-directory

So I pulled a specific configuration file (rsyslog.conf) off of a LOT of
hosts. I'm going to be managing it with [Puppet](), but before I do, I
need to know what's out there already lest it get overwritten. I used
[pssh](http://code.google.com/p/parallel-ssh/) with `cat` and an output
directory to grab the file from all 30 servers in question. Now, I've
got a directory with 30 files in it, and I need to figure out how many
different files (by contents) there are, and which ones differ.

~~~~{.bash}
find . -type f -exec md5sum '{}' \; | sort | uniq -d -w 36
~~~~

This will check the contents of each file by MD5 checksum, and print out
the (lexographically) first file in each group, along with its MD5 sum.
You can also strip off the uniq command, and see the list sorted by md5.

A GUI alternative would be to use
[fslint](http://www.pixelbeat.org/fslint/), which is a graphical tool
that can (among other things) display a list of the duplicate files
within a path or set of paths.
