Title: How to make software distribution secure
Date: 2010-09-17 12:42
Author: admin
Category: Ideas and Rants
Tags: linux, mac, packaging, security, software, windows
Slug: how-to-make-software-distribution-secure

We were seeing some strange behavior with Mac client machines on the
network lately, specifically with DNS queries (I'd guess that a lot of
it has to do with [Bonjour][]), but the discussion touched on the [DNS
Changer][] [trojan][] for Mac. I'd really never heard about it before,
and after some basic reading, it really got me thinking about the state
of software packaging, updates, and distribution. Granted, some of my
observations would require sweeping changes to how packaging is handled
(even on the \*nixes), and would require buy-in from more than just the
vendor and distributor (well, I guess MS can probably pressure ISVs to
do whatever they want), but seems to be the only way to keep
appliancization from becoming the solution to security issues. I've
written about this [before][], and a while ago in respect to [Linux][],
but here's my current take on what needs to be done to software
packaging to allow our machines to stay secure, no matter what OS they
run.

1.  **Allow packages to be installed as a user.** This is a mammoth task
    under Windows or Mac, but still an issue under Linux. The DNS
    Changer trojan is a case in point - there's no reason a "video
    codec" would need to be installed system-wide, and if that were
    simply installed user-specific, the malicious installer would never
    have the privileges to change system-wide DNS settings. This is also
    a big issue under Linux. Yum, apt, rpm, etc. should (if run as a
    non-root user) install packages in a user-local path under `/home`
    by default. Of course, this would mean many things would need to
    change in order to cope - perhaps even a change to the [LSB][] spec.
2.  **Warn about inconsistencies on package installation.** The package
    installation program should warn a user (whether installing packages
    system-wide or local to a user) if the package is going to modify
    system-wide files, i.e. files not specifically placed by that
    package and that package only.
3.  **Real package management for Windows and Mac** It's about time that
    Apple and Microsoft admit that people without billions in funding
    can come up with good ideas. Get rid of these Installer programs
    (the many many different ones). Each OS should pick a package
    format, develop a yum-like (or, even better, zypper-like) package
    management program that understands repositories. I don't know how
    they'd cope with the pervasive license keys and DRM in the non-nix
    world, but I'm sure they could figure out a way that still allowed
    sane package management. The idea here is that vendors run
    repositories and are responsible for their GPG keys, so trojans
    claiming to be an update to a given vendor's software would be
    rejected. Also, isn't it about time that you can update all your
    software on Windows or Mac through one tool?
4.  **Filesystem-based IDS for Windows and Mac** Assuming it will take a
    while to get everyone onboard with the packaging idea, and noting
    that users of these OSes like installing applications from arbitrary
    sources, there should be an OS-level feature to audit all filesystem
    changes made by untrusted/unsigned applications, and a way to alert
    the user to these changes if they appear suspisious (essentially
    what [Spybot Search & Destroy / TeaTimer][] do, but builtin to the
    OS).
5.  **Vendor support of packaging/repositories** - Along with the idea
    of repositories, vendors should have a trust or signing system for
    ISVs signing keys. If users are installing arbitrary software,
    making them trust an arbitrary key won't do anything to improve
    security. Microsoft and Apple need to run a CA that signs the
    package signing keys of their ISVs. The also - and here's the big
    one - need to have a parallel framework for "independent
    developers". I.e. something that doesn't cost any money for the
    packagers, and allows them to at least give a "this person is who
    they say they are" message.
6.  Finally, **Make package management pervasive** - Have a real push to
    apply the packaging and signing keys standard to all software for
    the OS.
7.  

On a final note, applicable to both the current state of Linux packaging
and my ideas about Mac and Windows... DNS is the ideal method of key
distribution (granted, yes, this just means that the security of the
packager's DNS records, and their servers and signing key, is just more
of an issue). But even with Yum and Zypper, it seems to me to be logical
that the packager's public key should be stored in a DNS record (or at a
URL stored in a DNS TXT record). That way, it wouldn't be up to an end
user to import and trust a key, they'd just have to trust the repository
(i.e. software.adobe.com) and the package manager would pull down the
key and verify that package X in software.adobe.com is, in fact, signed
by the software.adobe.com key.

  [Bonjour]: http://en.wikipedia.org/wiki/Bonjour_(software)
  [DNS Changer]: http://isc.sans.edu/diary.html?storyid=3595
  [trojan]: http://www.dnschanger.com/
  [before]: /2009/12/book-comments-the-future-of-the-internet-and-how-to-stop-it-by-jonathan-zittrain/
  [Linux]: /2008/10/my-biggest-problem-with-linux/
  [LSB]: http://www.linuxfoundation.org/collaborate/workgroups/lsb
  [Spybot Search & Destroy / TeaTimer]: http://www.safer-networking.org
