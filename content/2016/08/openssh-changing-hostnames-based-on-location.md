Title: OpenSSH changing hostnames based on location
Date: 2016-08-27 11:22
Author: Jason Antman
Category: Tech HowTos
Tags: openssh, ssh
Slug: openssh-changing-hostnames-based-on-location
Summary: How to change SSH hostnames based on guessed location
Status: draft

Yesterday I was doing some work on my laptop, SSHed in to my desktop ("phoenix"). As
always happens when I'm using my laptop from home, I kept getting connection errors...
because my ``~/.ssh/config`` on my laptop is setup with my dynamic DNS hostname and port
to reach my desktop, for any time I'm out of the house. But those don't work while
on the home network, and I got really tired of having to ``ssh 192.168.0.24``.

It turns out that, as long as your're using [OpenSSH >= 6.5](http://www.openssh.com/txt/release-6.5),
the ``ssh_config (5)`` file (typically ``~/.ssh/config``) supports a ``Match`` directive
that can execute system commands, and either match or not based on exit code.

I came up with relatively naive script that tries to determine whether or not I'm on my
home network based on a combination of ``resolv.conf`` settings, IP address and WiFi
SSID:

```bash
#!/bin/bash
# test if I'm on my home network,
# for SSH matching. Somewhat naive.
#
# For use in ~/.ssh/config Match directive;
# exit 0 if I'm at home, exit 1 otherwise
#
# To debug, run script directly as `bash -x am_i_am_home.sh`
########

# check that I've got the right nameserver and search domain; exit otherwise
grep -q 'jasonantman.com' /etc/resolv.conf || exit 1
grep '^nameserver' /etc/resolv.conf | grep '192.168.0.1' || exit 1

# check that I've got a 192.168.0. address; exit otherwise
ip addr | grep -q '192.168.0.' || exit 1

# check that I'm connected to one of my SSIDs; if so, exit 0 (match)
nmcli -t -f active,ssid dev wifi | grep -q '^yes:ObiWAN' && exit 0
nmcli -t -f active,ssid dev wifi | grep -q '^yes:WAP1' && exit 0

# assume not; no match
exit 1

```

This can be used in my ``~/.ssh/config`` to trigger an initial (internal network)
directive if it exits 0, and fall through to the external-network directive otherwise,
as shown below. The ``originalhost phoenix`` portion of the ``Match`` line ensures
that it's only executed if I ``ssh phoenix``, so it doesn't conflict with other
host directives.

```
# phoenix when at home
Match originalhost phoenix exec "/home/jantman/bin/am_i_at_home.sh"
     HostName phoenix
     Port 22

# fall-through - phoenix when abroad
Host phoenix
     HostName my_dynamic_hostname
     Port <something other than 22>
```
