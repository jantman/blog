Title: Quick Tip: Timestamping bash history
Date: 2013-06-11 07:09
Author: admin
Category: Software
Tags: bash, history, shell, timestamp
Slug: quick-tip-timestamping-bash-history

Here's a tiny little snippet that I have in my `.bashrc` which really
comes in handy when trying to figure out what I did on a system when.
One of the first things I do when (eek) building out or working on a
one-off machine (or setting up a new laptop/desktop, as I am right now)
is set this in bashrc for my user and root, so I can go back and
document the setup process with a little more ease and sanity. Just add
this (it's just a [strftime (3)](http://linux.die.net/man/3/strftime)
format string [according to the
docs](http://www.gnu.org/software/bash/manual/bashref.html#index-HISTTIMEFORMAT),
so adjust as desired) to `.bashrc`:

~~~~{.bash}
export HISTTIMEFORMAT="%F %T "
~~~~

and bash will store commented-out integer timestamps before each line in
`.bash_history` like so:

~~~~{.console}
#1370950005
less .bashrc
#1370950017
history 
#1370950279
tail -30 .bash_history 
#1370950293
exit
~~~~

the output of `history` now uses the specified time format:

~~~~{.text}
 997  2013-06-11 07:26:45 less .bashrc
 998  2013-06-11 07:26:57 history 
 999  2013-06-11 07:31:19 tail -30 .bash_history 
1000  2013-06-11 07:31:33 exit
~~~~


