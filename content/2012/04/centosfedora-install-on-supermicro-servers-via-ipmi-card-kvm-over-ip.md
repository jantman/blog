Title: CentOS/Fedora Install on SuperMicro Servers via IPMI Card KVM Over IP
Date: 2012-04-13 15:19
Author: admin
Category: Hardware
Tags: anaconda, centos, fedora, ipmi, kvm, linux, raritan, supermicro
Slug: centosfedora-install-on-supermicro-servers-via-ipmi-card-kvm-over-ip

I recently had to setup Fedora 16 to test something on a [SuperMicro
6015T-TV](http://www.supermicro.com/products/system/1U/6015/SYS-6015T-T.cfm)
1U "dual" server. This is a 1U enclosure with two separate servers in it
- based on the [SuperMicro
X7DBT](http://www.supermicro.com/products/motherboard/Xeon1333/5000P/X7DBT.cfm)
motherboards - each with an
[AOC-SIMSO+](http://www.supermicro.com/products/accessories/addon/SIM.cfm)
IPMI and KVM-over-IP management card. Every time I tried different
options for the kernel parameters (I was using Cobbler), I could get the
OS to boot, but once Anaconda started, I'd lose image ("No Signal") on
the IP KVM, and the serial console would go quiet. It took me about a
dozen tries before I found a mailing list reference to the "nomodeset"
option. This did the trick perfectly, and kept Anaconda working.
