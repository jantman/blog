Title: Syslog from KickStart / Anaconda
Date: 2010-03-24 13:52
Author: admin
Category: Tech HowTos
Slug: syslog-from-kickstart-anaconda

Yesterday I was installing a new machine at $WORK, and we'd been having
some spotty problems with [Anaconda][] not being able to find RPMs in a
specific repository. As a result, I was standing in the machine room at
a cart-mounted console, watching the output of the installation. Just as
I pressed the power button to give it a try, I realized that if the
conditions in the machine room aren't unpleasant enough, I probably
shouldn't have had those 3 bottles of water.

It took me about 4 seconds on Google to find out that KickStart files
support a `syslog` directive that sends all logging for the installation
process to a syslog server.

The directive in the KS file is quite simple:

    syslog=hostname

Hopefully this will be as much of a help to someone else who hasn't
noticed it yet...

I found this documented in the [RedHat/CentOS 5.1 Installation Guide.][]

  [Anaconda]: http://fedoraproject.org/wiki/Anaconda
  [RedHat/CentOS 5.1 Installation Guide.]: http://www.centos.org/docs/5/html/5.1/Installation_Guide/s1-kickstart2-startinginstall.html
