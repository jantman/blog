Title: ROUThost DNS problems; GoDaddy and Security through Obscurity
Date: 2009-02-25 11:07
Author: admin
Category: Miscellaneous
Tags: dns, godaddy, hosting, routhost, security through obscurity, support
Slug: routhost-dns-problems-godaddy-and-security-through-obscurity

The external-facing web site and (internal use) mailing list for the
[ambulance corps](http://www.midlandparkambulance.com) is hosted by
[ROUThost](http://www.routhost.com). Not my choice, it was inherited.
ROUThost, first off, appears to be a fly-by-night hosting provider that
just buys a few boxes in a colo facility. I should have known to raise a
stink when they say you need to fax a copy of your driver's license to
get SSH turned on, and that you have to agree - in legalese - not to
mess with anyone else's configs. Well, last night, DNS for the site went
down. As in nothing, wouldn't resolve at all. I submitted a ticket
online for ROUThost's "24x7" support - by the way, they don't have a
phone number, only an online ticket form. After 2h 34m 40s of downtime,
the issue resolved itself and I downgraded the ticket from "critical" to
medium. Now, 11 hours later, it still hasn't been replied to. And my
emails to support and management - 2 hours ago - are unanswered.

Once the problem started, I knew the yearly contract with ROUThost was a
bad idea - even at $35/year USD. So, given the great experience I've had
with them as registrar for my myriad domains, I took a look at
[GoDaddy's Site](http://www.godaddy.com). They offer shared
hosting at around $4/month (for shared on a Linux box) and are currently
offering some deals, so I figured it would be a good idea. I know and
trust GoDaddy's support, and have had an account with them for *quite
some time*.

The ambulance corp's web site, hosted through ROUThost, does essentially
three things; provide a minimal web presence (the whole web root is
probably < 1Mb minus the photo albums), five e-mail forwarders for the
officers and a [GNU
MailMan](http://www.gnu.org/software/mailman/index.html) mailing list
for internal business. Unfortunately, I couldn't find anything in their
"features" list mentioning MialMan or any other listserv, or even what
MTA/MDA they run.

I put a call in to GoDaddy "Sales/Support". The poor guy had never heard
of MailMan, but asked "one of the hosting guys" and was told it would
only be supported on dedicate hosting accounts. Not exactly financially
feasible for a mailing list with 30 subscribers, maybe 2 messages a day,
and a monthly HTTP transfer of under 20Mb. I was told their shared
hosting packages don't include any mailing list/listserv software,
though they include every CMS and language known to man. Hell-bent to
get away from ROUThost, I then asked if they ran an MDA that supported
piping mail to a command, as can be done with .procmailrc. After a brief
hold (not to sound cynical, but I'm sure the gentleman was looking up
"MDA") he came back on the line and told me they didn't. I then switched
to problem-solving mode and asked what MTA and MDA they were running.
Another brief hold, and I was told *"I can't tell you that"*. Speechless
for a moment, I asked what that meant; *"we don't give out that
information"*. Just about ready to begin explaining SMTP headers, I gave
up and thanked him for his time.

Ok, so Sales probably doesn't understand SMTP headers. I'd considered
trying to find mail from a GoDaddy Linux hosted box and check the
headers, but I figured I couldn't do that before the call ended. So, now
I'm left with a dilemma. ROUThost is not, in my opinion, reliable, and
their support is flat-out nonexistent. 11 hours is far too long to wait
for a reply to a "critical" ticket when someone claims 24x7 support.
However, by previous experience, GoDaddy would be my next choice - but
not only do they ot support mailing lists - arguably the most used
feature of our current hosted account - but they won't even tell a
customer what MTA they're running. I'm too let down by this to telnet 25
on one of their boxes and see what happens.

So what's left? I guess waiting until (hopefully some time within the
next few weeks) I upgrade to Optimum static IP at home, and consider
running it all there (and hope mains power never goes out for more than
30 minutes?)
