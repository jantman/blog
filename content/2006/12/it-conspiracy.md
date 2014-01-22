Title: IT Conspiracy
Date: 2006-12-15 19:05
Author: admin
Category: Ideas and Rants
Tags: dynamic IP, fios, internet, ISP, verizon
Slug: it-conspiracy

The "true" Internet is based on freedom. The original 'net, a system of
BBS's and mailservers each with their own address format, was free.

More and more, that freedom is fading away. We have ads. Popups. Content
filters. KGB-esque ISP's. The great advent of centralized,
high-bandwidth IPS's, instead of person-to-person dial-up connections,
has changed what the Internet is.

Now, I don't want to sound like I'm bashing progress. I'm vary glad to
have a home internet connection of 10 mbps down / 1.5 mbps up.

The problem that I have is that the concept of freedom on the Internet
is based on its' distributed architecture. In the old days, with dial-up
links, there was no real backbone, per se, and the 'net was really owned
by its' users, by everyone.

<span style="font-weight: bold;">Part I: The Block</span>

In 2006, we see an increasing trend towards the 'net being owned and run
by monopolies. Not to group them together, but companies such as Google,
AOL, and Microsoft aim to provide an all-encompassing Internet
experience. The former is a wonderful resource, while the latter two are
evil. However, as these monsters evolve, and the Internet moves from a
distributed architecture to that of one central pipeline, is freedom
gradually fading away?

The case in point, and impetus for all this, was a recent event:  
When I got my first high-bandwidth home connection, CableVision's
Optimum Online, it was amazing. And, though I'm sure they didn't know
it, it was perfect. My "dynamic" IP was leased for a few months at a
time, so my domains just pointed right to it. I'd change them when it
rolled over. Aside from the rollover day, and the fact that my IP didn't
reverse-validate (only a problem when trying to run a mail server,
though I solved that by relaying outgoing mail), I had a completely
functional connection.

Then, FiOS exploded on suburbia. Fiber-optic, high-bandwidth lines to
the residence, claiming 5mbps down/1mpbs up. I was hooked. Verizon
installed it on the first day it was available. The technician was still
as amazed as I was, and was a real technician, not one of the trained
morons that take over once the bugs are worked out.

The connection speed was amazing. Then I went to change over my domain
names. Could it be possible? Yes. A conspiracy. Optimum had in their TOS
that you couldn't run a server, but I always figured it was a way to get
rid of unruly customers. Well, Verizon thought otherwise. All incoming
requests were blocked on port 80. Yes, they were attempting to actually
prevent anyone from hosting their own web sites.

Well, simple fix. I had my domain names registered through GoDaddy, so I
just bound Apache to port 10011 (an unused port) and forwarded my
domains to http://xxx.xxx.xxx.xxx:10011. Beautiful. For about 24 hours.
Then they stopped working. I was in a panic. I had returned to college,
and had no access to my machines. I frantically called my mother at
home. The her 'net was working. She could ping my machines. What could
it be?

It took me a minute to think of it. I instructed her on how to find the
WAN IP. She read it off. Sure enough, it changed. I updated the IP,
logged in, and, of course! The Verizon DHCP lease was less than 72
hours. Enter dynDNS.org, a wonderful (and free service) that provides
DNS resolution with a client program resident on one of your servers or
routers, keeping their DNS records for you up-to-date. A bit of a
kludge, but now jantman.dyndns.org pointed to my IP, and jasonantman.com
pointed to jantman.dyndns.org:10011.

For over a year, it's worked. I've harbored resentment against Verizon,
but at over 100% more expensive, I can't possibly afford their static IP
FiOS. So, I've just been infinitely upset at Verizon's desire to quash
free speech, freedom of use and, in my opinion, part of what the
Internet's about.

<span style="font-weight: bold;">Part II: The Conspiracy</span>

Since then, my father (who works at a very large state agency) has never
been able to view my web page. Nobody else has complained of this
problem. I get indexed by the search engine bots, and get plenty of
hits. But my father can't see my web site.

Now, I know that his entire organization, (supposedly back-end also) is
run on Windoze, or, as I prefer to call it, the Blue Plague. So, I was
already suspicious of their IT infrastructure.

Well, finally, I gave in, and asked him to e-mail his IT guys. The
response that I got: They block any web requests to any port other than
80.

From a security standpoint, I can see this as being a potentially useful
trick. However, the sheer reality of it is baffling. Residential ISP's
block any requests to a server on port 80, and meanwhile, large
companies block all outgoing HTTP requests to anything other than port
80.

At what point will the users take back the Internet, and put ourselves
in control again? How is it that we have allowed pop-ups, spyware, and
our ISP's and corporations telling us what content they want us to get,
and what content we can provide to other people?

When will we users finally stand up and say, "This is what we want. This
is what is expected of you, and we will not let you tell us otherwise"?
