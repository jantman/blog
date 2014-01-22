Title: Managing G1 Proliant Servers with modern Linux
Date: 2007-03-01 16:27
Author: admin
Category: Tech HowTos
Tags: compaq, hp, hpadu, hpasm, linux, management, proliant, psp
Slug: managing-g1-proliant-servers-with-modern-linux

Not much of an "upgrade" for anyone who's in IT, but jasonantman.com is
currently being upgraded from old desktops used as servers to a pile of
generation-1 (G1) HP/Compaq Proliants. I know that there are utilities
for Linux to manage the servers, specifically control fan speed and
monitor hardware-level health for Linux. However, the most recent
download on HP's site is for SLES9. All of my boxes will be running
openSuSE 10.2, and the SLES9 version wouldn't install on them.

After an hour long phone call to HP support, I ended up speaking with
Paulo, the third support person I was transferred to. \#1 read off the
web site, \#2 knew what Linux was, but Paulo (\#3) actually told me that
he was experimenting with installing HPASM (HP's server
administration/management utility) on an older Proliant as well. He
spent about half an hour walking me through it. Here's what I found:

The most compatible version of HPASM (I guess it's some hidden feature
for people who know it) is the version for the DL380 G4. Paulo
instructed me to download this RPM from their site. I did, choosing the
SLES10 (x86) download (hpasm-7.7.0-115.sles10.i586.rpm). This installed
fine. Running `hpasm status` from the command line asks us to activate
it first. Do the activation. Now, running `hpasm status` still asks us
to activate. Paulo confirmed this as happening on his machine too. Try
`/etc/init.d/hpasm status` and you should see that all of the modules
are working.

Now, the install is complete. I'm not sure if the SNMP works, but it
should as long as your snmpd is running. The `hpasm activate` command
modifies snmpd.conf appropriately. and you will be queried for the
currect configuration information.

To give it a test, run `hplog -f` or `hplog -p` and you should see fan
and power status, respectively.

Paulo also told me that I could download the hpadu package (also DL380
G4 / SLES10) to get array diagnostics, He warned me that some of the
install scripts in HPADU look for the web management homepage, which we
haven't installed. To get around this, install the HPADU RPM file
(hpadu-7.70-12.linux.rpm)
`rpm -ivh --force --nodeps --noscripts hpadu-7.70-12.linux.rpm`. Be
aware, though, that this package is supposed to be web-based. It
installs to /opt/hp/hpadu.

The web interface, luckily for me, is written in PHP. It is pretty
complex so it might take me a while to figure out the workings, but when
I do, I'll post as much info as I can on how to make a CLI interface, or
where one exists if I can find it.

Also, I'll most likely develop a Python check script to use with
[Nagios][] to monitor most of the hpasm-enabled components.

For the use of anyone else, here are some of the links that HP Support
sent me after the call:

Link for users guide for Proliant Support Pack, which includes
documentation on HPASM from the CLI:

[http://h18000.www1.hp.com/support/files/server/us/WebDoc/720/psp-users-guide.pdf][]

Product manuals:

[http://h20180.www2.hp.com/apps/Nav?h\_pagetype=s-003&h\_lang=en&h\_cc=us&h\_product=241435&h\_page=hpcom&h\_client=z-a-r1002-3&cc=us〈=en][]

ML370 G1

[http://h20000.www2.hp.com/bc/docs/support/UCR/SupportManual/TPM\_143091-004/TPM\_143091-004.pdf][]

  [Nagios]: http://www.nagios.org
  [http://h18000.www1.hp.com/support/files/server/us/WebDoc/720/psp-users-guide.pdf]:
    http://h18000.www1.hp.com/support/files/server/us/WebDoc/720/psp-users-guide.pdf
  [http://h20180.www2.hp.com/apps/Nav?h\_pagetype=s-003&h\_lang=en&h\_cc=us&h\_product=241435&h\_page=hpcom&h\_client=z-a-r1002-3&cc=us〈=en]:
    http://h20180.www2.hp.com/apps/Nav?h_pagetype=s-003&h_lang=en&h_cc=us&h_product=241435&h_page=hpcom&h_client=z-a-r1002-3&cc=us〈=en
  [http://h20000.www2.hp.com/bc/docs/support/UCR/SupportManual/TPM\_143091-004/TPM\_143091-004.pdf]:
    http://h20000.www2.hp.com/bc/docs/support/UCR/SupportManual/TPM_143091-004/TPM_143091-004.pdf
