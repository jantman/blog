Title: Nagios and check plugins run as root
Date: 2009-11-05 17:05
Author: admin
Category: Miscellaneous
Tags: Nagios
Slug: nagios-and-check-plugins-run-as-root

No matter how much we may not like it, and no matter how insecure it can
potentially be, we occasionally have to run Nagios check scripts
(written in scripting languages) as root. (On a side note, this method
is also used for my
[MultiBindAdmin](http://multibindadmin.jasonantman.com/) project's DNS
file push). Here's how to do it:

1.  Write your check script in the language of your choice and test as
    root.
2.  Grab
    [setuid-prog.c](https://github.com/jantman/nagios-scripts/master/setuid-prog.c)
    from GitHub.
3.  uncomment the DEFINE for FULL\_PATH, change the string to the full
    path to your script.
4.  **Be sure** your script is owned by root, and is chmod **at most**
    755.
5.  Compile setuid-prog.c:
    `gcc -o {check_script_name}-wrapper setuid-prog.c`
6.  Put the resulting binary in your plugin directory.
7.  Assuming your checks run as user nagios and group nagios, chown the
    binary to root:nagios and chmod 4755.

This allows the use of the SUID bit with scripts.

**Use at your own risk.** I only recommend this on systems where the
Nagios account is strongly authenticated, and where ALL users are
trusted.
