Title: Quick and Simple Timestamping of Debug Logs
Date: 2011-09-08 07:06
Author: admin
Category: Software
Tags: debugging, logs, puppet, sysadmin, timestamp
Slug: quick-and-simple-timestamping-of-debug-logs

I've been having some issues that may be
[Puppet](http://puppetlabs.com/)-related. Unfortunately, Puppet (at
least the old 0.25.4 client that I'm running) doesn't timestamp the
debug logs sent to stdout. I know it's hanging somewhere, but I need
concrete numbers to look at. Here's a wonderfully simple bash script
that timestamps everything sent to it on stdin, and echoes it back to
stdout:

~~~~{.bash}
#!/bin/bash

DATECMD='date +%H:%M:%S'

while read line; do
    echo -e "$($DATECMD) $line"
done
~~~~

Call it as simply as: `command | ~/bin/ts`, or maybe like
`command 2>&1 | ~/bin/ts | tee foo.log`. Dead simple, but very helpful
when the developers didn't think to timestamp debug log output.
