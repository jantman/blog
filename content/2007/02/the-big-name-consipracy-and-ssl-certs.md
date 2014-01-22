Title: The Big Name consipracy - and SSL certs
Date: 2007-02-06 02:28
Author: admin
Category: Ideas and Rants
Slug: the-big-name-consipracy-and-ssl-certs

So I decided to setup SSL on my Apache server. After looking around for
ages, it seems that the answer to SSL Certs is that I need to buy one.
There doesn't seem to be any CA out there who will provide free certs
that are accepted by most browsers.

So, this brings me into one of my favorite diatribes. The "Big Name"
Conspiracy, as I like to call it.

Many many years ago, leading computer researchers began to connect their
systems into a worldwide (or at least nationwide) network. The admin of
each machine was trusted. There was a hosts.txt file distributed. Then
computers came to the home, and with them, serial modems and
connectivity. In the brief time before the 'net turned into a wasteland,
it was free. Free as in if you had a phone line, the hardware, and the
knowledge, you could setup your own BBS or other server.

Skip forward to 2007. I pay exorbitant rates (well, about $40/month) for
a residential fiber-optic connection. A few people I know can't view my
web site. Why? Because Verizon, my ISP, blocks incoming traffic on port
80 so that I can't run a server. And they won't give me a static IP, so
I can't run a server. Thankfully, the folks at DynDNS.org are fighting
for us, and they give me free DNS, which I can even forward my domain
name to. To get around Verizon, I forward HTTP traffic to a high-number
unused port. Well, what do you know, a number of corporate Internet
filters block all web traffic going to ports other than the defaults.

I wanted to send mail from a Linux machine. So, I configured Postfix and
sent mail. Worked perfectly to a few addresses, but AOL, Verizon,
Hotmail, Gmail, big companies - forget it. Rejected. Why? Because I have
a dynamic IP, and my domain name doesn't reverse-validate, so I must not
be a legitimate user. There's no way around it. Try sending mail from
you@yourdomain.dyndns.org - I have yet to find a mailserver that will
accept it.

What happened to the community environment of the 'net? Yes, I know,
it's all in the name of "bettering" the 'net, reducing spam, etc. But I
have yet to find anyone who will whitelist my dynamic IP.

Maybe I'm just obtuse. Or angry. But it seems to me that there is a
"conspiracy", perhaps unspoken, among the Big Names out there to
centralize the Internet, to prevent [I]people[/I] from participating.

I know I'm not the only person who has noticed this. While there are
many people and companies out there valiantly fighting for freedom on
the Internet, it seems that the majority of big companies, ISPs, hosting
providers, etc. want the 'net to be a one-way medium: content is
provided by those who can pay for leased lines and IP blocks, and
everyone else looks at it.

Running a group of servers - web, SMTP, IMAP, etc. - on a dynamic IP, I
am acutely aware of exactly how much modern Internet technology relies
on the fact that anyone who's [I]providing[/I] the content has a static
IP - and can pay the cost associated with it.

Getting back to the SSL cert, why isn't there a reputable authority who
provides free certificates? I have unlimited free long distance calls, I
would be more than willing to call the DNS contact number for every
applicant to validate.

And why hasn't anyone developed a method of making a dynamic IP "look"
static to the rest of the world - surely IANA should set aside a massive
block of IPv6 for this, if not IPv4.
