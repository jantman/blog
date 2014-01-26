Title: February 26, 2008
Date: 2008-02-26 11:32
Author: admin
Category: Projects
Tags: GigE, microsoft, mythtv, sata, storage
Slug: february-26-2008

Well, while I haven't made much progress on anything interesting -
mainly my NMS comparison or any of my other projects - due to my busy
schedule, I did get an hour or two to clean up my network at the
apartment, swapping out my 24-port Linksys switch in my room for the
5-port Netgear previously used for printing. I threw all of the printers
and the print server on their own VLAN on the main 3com switch.

I've also started thinking more about [MythTV](http://www.mythtv.org/) -
I use it for TV in my room (feeding a grossly insufficient 21" CRT
monitor), and my roommate has a Dell GX270 by the big TV in the living
room, though it was running Freevo (and now has a dead tuner and no RAM,
or something like that). So, I decided that I might do things right -
drop a 5- or 8-port GigE switch in the apartment, put GigE NICs in the
two boxes with tuners (putting MythTV on the GX270 also), and setting up
a centralized system. The problem is that the ideal solution would be a
single dedicated back-end system for storage and control, with the two
tuner/video out boxes just providing A/V I/O. Unfortunately, the two
boxes with tuners are both high-spec'ed P4's, and I'm not sure what I
can come up with in terms of a server for the backend.

Now, *the question for anyone who may be
reading* - I'd like to setup a good amount (1-2TB) of storage for
this. My roommate wants a RAID configuration, but I don't see the need
for videos - if I lose my TV recordings, I set MythTV to record it again
the next time it's on. Anyway, I have an 8-bay external SCAI enclosure
and cards in all of the servers, but SCSI disks are expensive. I was
thinking of going to SATA 3.0. Most likely, I'd get some sort of 4-8
disk enclosure, start with 1-3 disks in the 400-750GB range.

So, the question - what type of system specs would be needed to stream
audio and video, uncompressed, perhaps even HDTV (we have the TV and
cable box, would just need an HD tuner) to remote storage over the
network? I was thinking of doing either a Linux master MythTV backend
with eSATA cards, or letting each TV computer be its' own backend, and
then doing Solaris/ZFS with iSCSI or ATAoE. Any suggestions? I'm pretty
much thinking of using a PowerEdge 2550 for this.

Anyway, I'm also filling up my backup disks at home, and don't want to
shorten my expiration cycle. My nightly backup runs put quite a strain
on my main Fast Ethernet LAN, so I've been planning for a while on
moving to GigE. My thought at home is to setup a second, separate GigE
switch/lan, with GigE NICs in all of the servers. Not exactly cheap, but
I can pickup a Linux-/Solaris-compatible Negear GA311 for around $40, in
addition to the Intel Pro/1000 XT and Asante GigaNIC that I already
have. The problem here is finding a good GigE switch - I'd really like
something with Telnet, SNMP, VLANs, the works.

In other news, I highly recommend reading the [Groklaw story on
Microsoft's latest pledge for
interoperability](http://www.groklaw.net/article.php?story=20080221184924826).
I especially liked the one quote from the [ECIS](http://www.ecis.eu/)
statement:  

> For years now, Microsoft has either failed to implement or has
> actively corrupted a range of truly open standards adopted and
> implemented by the rest of the industry. Unless and until that
> behaviour stops, today's words mean nothing.
>
> More fundamentally, today's announcement is still all about the rest
> of the world interoperating with Microsoft on Microsoft's own terms,
> not the other way around.

There's even links to *ten* previous Microsoft statements promising
interoperability.  

> The thing is, this is a promise to interoperate with old-fashioned
> competitors. It doesn't enable interoperability with the GPL, which is
> not compatible with patent licenses, and that is Microsoft's true
> competition.
> </p>

From Michael Cunningham, VP and General Counsel of Red Hat:  

> Eight years ago the U.S. regulatory authorities, and four years ago
> the European regulators made clear to Microsoft that its refusal to
> disclose interface information for its monopoly software products
> violates the law. So, it is hardly surprising to see even Microsoft
> state today that “interoperability across systems is an important
> requirement” and announce a “change in [its] approach to
> interoperability.” Of course, we’ve heard similar announcements
> before, almost always strategically timed for other effect. Red Hat
> regards this most recent announcement with a healthy dose of
> skepticism. Three commitments by Microsoft would show that it really
> means what it is announcing today:
>
> -   Commit to open standards: Rather than pushing forward its
>     proprietary, Windows-based formats for document processing, OOXML,
>     Microsoft should embrace the existing ISO-approved, cross-platform
>     industry standard for document processing, Open Document Format
>     (ODF) at the International Standards Organization’s meeting next
>     week in Geneva. Microsoft, please demonstrate implementation of an
>     existing international open standard now rather than make press
>     announcements about intentions of future standards support.
> -   Commit to interoperability with open source: Instead of offering a
>     patent license for its protocol information on the basis of
>     licensing arrangements it knows are incompatible with the GPL –
>     the world’s most widely used open source software license –
>     Microsoft should extend its Open Specification Promise to all of
>     the interoperability information that it is announcing today will
>     be made available. The Open Specification Promise already covers
>     many Microsoft products that do not have monopoly market
>     positions. If Microsoft were truly committed to fostering openness
>     and preventing customer lock-in, it would extend this promise to
>     the protocol and interface information it intends to disclose
>     today. There is no explanation for refusing to extend the Open
>     Specification Promise to “high-volume” products, other than a
>     continued intention on Microsoft’s part to lock customers into its
>     monopoly products, and lock out competitors through patent
>     threats.
> -   Commit to competition on a level playing field: Microsoft’s
>     announcement today appears carefully crafted to foreclose
>     competition from the open source community. How else can you
>     explain a “promise not to sue open source developers” as long as
>     they develop and distribute only\*/ “non-commercial”
>     implementations of interoperable products? This is simply
>     disingenuous. The only hope for reintroducing competition to the
>     monopoly markets Microsoft now controls – Windows, Office, etc. –
>     is through commercial distributions of competitive open source
>     software products.

Amen!!!
