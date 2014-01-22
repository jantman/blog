Title: How to get actual login username when using sudo su
Date: 2011-01-05 11:48
Author: admin
Category: Tech HowTos
Tags: linux, login, sudo, username
Slug: how-to-get-actual-login-username-when-using-sudo-su

I've had the need to find out the actual username of someone logged in
and working as root (via `sudo su -`) to [put it into a subversion
commit message][]. This quick little bash script does the trick, and
just echos the username.

~~~~{.bash}
#!/bin/bash

PID=$$ # get PID of current process
LogUID=`cat /proc/"$PID"/loginuid` # get loginuid of current process
username=`getent passwd "$LogUID" | awk -F ":" '{print $1}'` # translate loginuid to username
echo "$username"
~~~~

  [put it into a subversion commit message]: /2011/01/client-side-subversion-commit-message-hooks/
