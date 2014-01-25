Title: Client-side subversion commit message hooks
Date: 2011-01-05 11:23
Author: admin
Category: Tech HowTos
Tags: linux, puppet, subversion, svn
Slug: client-side-subversion-commit-message-hooks

While I know this isn't best practice, since we use LDAP-based auth for
our Linux boxes (including a sudoers file based on LDAP group
membership), we usually do work on some boxes as root (`sudo su -`).
This includes our [puppetmaster](http://www.puppetlabs.com/), where
configs are kept in subversion and edited as root. The one problem with
this is how to get the username of the actual committer, not root, in
subversion messages.

The theory that I came up with is a [shell script that finds out who the
actual user
is](/2011/01/how-to-get-actual-login-username-when-using-sudo-su/), and
then tacking this onto the beginning of the subversion commit message
(since there's no real way to do client-side hooks in subversion). While
I struggled with subversion's lack of good client hooks, I came up with
a theory based on a script that preloads svn-commit.tmp and then calls
the text editor. It's actually quite simple.

First, in your .bashrc or wherever you setup environment variables,
`export SVN_EDITOR=/usr/local/bin/svnPreCommitClientHook.sh`. This way,
every time you run `svn commit`, instead of calling your text editor
with `svn-commit.tmp` as an argument, the bash script will do what it
needs to (commit message preloading) with svn-commit.tmp and *then* call
your editor to finish the message.

/usr/local/bin/svnPreCommitClientHook.sh:

~~~~{.bash}
#!/bin/bash
LOGNAME=`/usr/local/bin/getLogname.py` # script to get user's actual login name, even if using sudo su
echo -e "\nBY: $LOGNAME" > svn-commit.foo
cat svn-commit.tmp >> svn-commit.foo
mv svn-commit.foo svn-commit.tmp
"$EDITOR" svn-commit.tmp
~~~~

Using this method, running `svn commit` will pull up your text editor
with "BY: username" already inserted in the commit message.
