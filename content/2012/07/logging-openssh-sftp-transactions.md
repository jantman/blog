Title: Logging OpenSSH SFTP Transactions
Date: 2012-07-16 08:47
Author: admin
Category: Tech HowTos
Tags: logging, openssh, sftp, ssh
Slug: logging-openssh-sftp-transactions

I just came across a really handy post on [David
Busby](https://plus.google.com/117561367404774597588/posts)'s blog:
[Enable logging in the SFTP subsystem -
Oneiroi](http://blog.oneiroi.co.uk/linux/enable-logging-in-the-sftp-subsystem/).
From OpenSSH 4.4 on, you can pass arguments to Subsystem calls, and the
sftp subsystem supports logging to an aribtrary syslog facility and
priority. Simply adding a line like:

~~~~{.text}
Subsystem       sftp    /usr/libexec/openssh/sftp-server -f LOCAL5 -l INFO
~~~~

and the appropriate lines to your syslog config will give you a handy
transfer log like:

~~~~{.text}
Jul 16 09:22:25 hostname sftp-server[2058]: session opened for local user jantman from [A.B.C.D]
Jul 16 09:22:26 hostname sftp-server[2058]: open "/home/jantman/temp/sftp_test" flags WRITE,CREATE,TRUNCATE mode 0666
Jul 16 09:22:45 hostname sftp-server[2058]: close "/home/jantman/temp/sftp_test" bytes read 0 written 1464813
Jul 16 09:23:08 hostname sftp-server[2058]: session closed for local user jantman from [A.B.C.D]
Jul 16 09:27:50 hostname sftp-server[2309]: session opened for local user jantman from [A.B.C.D]
Jul 16 09:27:50 hostname sftp-server[2309]: open "/home/jantman/temp/sftp_test" flags READ mode 0666
Jul 16 09:27:54 hostname sftp-server[2309]: close "/home/jantman/temp/sftp_test" bytes read 1464813 written 0
Jul 16 09:27:54 hostname sftp-server[2309]: session closed for local user jantman from [A.B.C.D]
~~~~
    
If you have syslog write these logs to their own file, remember to setup
log rotation for them.

Unfortunately, I'm not aware of any way to log SCP file transfers.
