Title: NSA Targeting SysAdmins
Date: 2014-03-22 09:38
Author: Jason Antman
Category: Ideas and Rants
Tags: nsa,government,privacy,security
Slug: nsa-targeting-sysadmins
Summary: Newly leaked documents reveal NSA is targeting SysAdmins - disturbing new information.

I try not to rant too much, but I feel that this one was needed. If you're looking for
objective, technical information, skip this one.

When I was younger and more naive, I had near complete trust in the US government. There's a Constitution,
and they abide by it, and so do I. Since 2001, that feeling has eroded a bit. Since 2008, it's eroded even
more. But the documents leaked by [Edward Snowden](http://en.wikipedia.org/wiki/Edward_Snowden) have been
the 'icing on the cake'. I know there's disagreement about whether what he did was right or not - I'm pretty
decided on how I feel, but I know many others who feel that he should be taken out and shot - but one thing
that's no longer deniable is, since he released those documents, it's come to light that the US government
is routinely performing unconstitutional acts in the furtherance of "national security."

I feel like many people, who said over and over again that it could never get to this point, that the
Government might cut some corners but they'd never blatantly do things like [mass collection of cellular data](http://www.washingtonpost.com/world/national-security/agencies-collected-data-on-americans-cellphone-use-in-thousands-of-tower-dumps/2013/12/08/20549190-5e80-11e3-be07-006c776266ed_story.html),
[tracking the physical location of cell phones worldwide](http://www.washingtonpost.com/world/national-security/nsa-tracking-cellphone-locations-worldwide-snowden-documents-show/2013/12/04/5492873a-5cf2-11e3-bc56-c6ca94801fac_story.html), or [tapping into the networks of private companies like Google and Yahoo](http://www.washingtonpost.com/world/national-security/nsa-infiltrates-links-to-yahoo-google-data-centers-worldwide-snowden-documents-say/2013/10/30/e51d661e-4166-11e3-8b74-d89d714ca4dd_story.html). It seems that
every new document leaked is worse than the last. I refuse to accept the arguments that this is all "legal",
they simply don't keep up with the times. I couldn't care less if the government reads my postal mail (which
they still need an actual warrant for, AFAIK) - they probably get the same credit card and siding offers anyway.
I do, however, care that the government - out of their own self-interest and excitement at near-effortless surveillance -
refuses to extend the same protections that wireline phone calls and postal mail get to their electronic and
wireless equivalents.

When it came to light that the NSA [paid $10M to put a backdoor in RSA encryption](http://www.reuters.com/article/2013/12/20/us-usa-security-rsa-idUSBRE9BJ1C220131220)
I was astonished. Late last year a number of other deals came to light, where the NSA paid or extorted software
and hardware manufacturers to intentionally introduce flaws in security to make it easier for the NSA
to gain access. The worst part is these weren't "master passwords" available only to the NSA; for the most
part, they appear to be mathematical flaws known to the NSA, but just as easily discovered by our enemies.
This part seems to have been glossed over by the media... the consequences of some mathematician
or security researcher discovering those flaws and selling them to a national enemy or terrorist
would be flat-out devastating to the country and economy. Our government deliberately put a flaw in
an encryption standard, and then used its' influence via NIST, the National Institute of Standards
and Technology, to [recommend that standard for use](http://arstechnica.com/security/2013/09/the-nsas-work-to-make-crypto-worse-and-better/)
including by banks, e-commerce sites and financial institutions.

What has me even more upset, though, is the recent revelation that the NSA is [systematically targeting
the private, personal accounts of system administrators to gain access to their employers' networks](https://firstlook.org/theintercept/article/2014/03/20/inside-nsa-secret-efforts-hunt-hack-system-administrators/). The bulk of the information came from an internal classified blog entry of an NSA employee,
[available as a PDF](https://s3.amazonaws.com/s3.documentcloud.org/documents/1094387/i-hunt-sys-admins.pdf)
(or [local copy](/GFX/i-hunt-sys-admins.pdf)). It's pretty technical, but it's also a startling view into
both the mindsets of *individuals* within the NSA, and the organization's overall goals. Just two of the many
worthy excerpts:

> (S/SI//REL) One of the coolest things about it is __how much__ data we have at our fingertips. If we
> *only* collected the data we knew we wanted... yeah, we'd fill some of our requirements, but it is
> a whole world of possibilities we'd be missing! It would be like going on a road-trip, but wearing a
> blindfold the entire time, and only removing it when you're at one of your destinations... yeah,
> you'll still see stuff, but you'll be missing out on the entire journey!

So... ok, they're admitting that they collect more data than they want (or legally can?). This person's
blog series is about "using passive collect to identify/enable CNE efforts" (CNE being Computer Network
Exploitation), which is also implying that they have access to massive amounts of data from non-target
persons, including American citizens.

Within the document, multiple references are made to the [QUANTUM](https://firstlook.org/theintercept/article/2014/03/12/nsa-plans-infect-millions-computers-malware/)
program which seems to be viewed as, in short, a tool that lets the NSA input someone's Facebook,
webmail, or other online service account, and take control of the computers they use to access it...

Now, for people in my line of work, the more troubling part:

> Now, fade off with me into dream-land. Pretend that we had some master list. This master list
> contained tons of networks around the world, and the personal accounts of admins of each of
> those networks. And any time you wanted to target a new network, you could just find the admin
> associated with it, queue his accounts up for QUANTUM, get access to his box and proceed to pwn
> the network. Wouldn't that be swell?
>
> (S/SI//REL) Well, you can stop dreaming my friends, I think it's possible (at least kinda partially).

So... we're talking about deliberately targeting the personal accounts of innocent third parties,
in order to compromise their credentials to also innocent networks, in order to eventually
gain access to the information of a target. This seems so horribly illegal I can barely
explain. It's also a direct affront to the people in my industry who have an ethical obligation
to protect the data of their employers, customers and users against illegal disclosure. And,
maybe even more troubling, it's being perpetrated by other people "in our industry", other
technical people, who obviously have a very clear picture of exactly what they're doing.

My first thought was to make an analogy between our resposibility as those "with the keys to
the kingdom" to a more legally entrenched privacy, like that between a doctor and their patient,
or between a lawyer and their client, that would be much more obviously illegal for the government
to breach. But, apparently that's an all-too-correct analogy, since it came to light last month
that the [NSA was intercepting privileged lawyer-client communications through the use of a
foreign intermediary, namely Australia](http://www.nytimes.com/2014/02/16/us/eavesdropping-ensnared-american-law-firm.html).
Given the intelligence allicances between the US, the UK and Australia, and the scope of what
has been already disclosed, I find it entirely probable that in all of these leaked documents
that discuss doing this to "foreign" entities only, the reality is that to do the same to US
citizens, it's as simple as logging in to the Australian or UK equivalent system.

This is truly disturbing to me. I continue to feel that (1) if the NSA had provable cause to
collect this information, they'd obtain a warrant like the Constitution says they have to,
and (2) their electronic data collection is the equivalent of wiretapping every phone in the
country and hoping for something useful - which has been continually held to be unconstitutional,
but because of the nature (already digital) of electronic communications, it's actually feasible
to do.

On a related note, a while ago I enabled [TOTP](http://en.wikipedia.org/wiki/Time-based_One-time_Password_Algorithm)-based
two factor authentication on a number of my accounts (Google, GitHub, AWS, etc.) to try
and keep them more secure against the possibility of a password compromise. Yes, that still works
to keep an unscrupulous person out of them. However, if [NSA officials use classified systems to
spy on love interests](http://www.washingtonpost.com/blogs/the-switch/wp/2013/08/24/loveint-when-nsa-officers-use-their-spying-power-on-love-interests/),
it's entirely possible that an unscrupulous NSA employee (or even worse, someone who manages to
compromise the NSA's systems? Though I imagine they only use in-house-developed security for now-obvious reasons)
could decide to compromise an individual's accounts for personal gain. Given all this news, I
find it highly unlikely that such an event would ever be reported to the proper oversight authorities,
let alone become public knowledge or known to the victim.

However, if we look at some of the information about what the NSA is doing, like their
[NSA's Utah Data Center](http://www.wired.com/threatlevel/2012/03/ff_nsadatacenter/all/)
and their plans for an [encryption-cracking quantum computer](http://www.theregister.co.uk/2014/01/03/snowden_docs_show_nsa_building_encryptioncracking_quantum_system/),
and assume that they probably have a datacenter full of FPGAs, it's entirely conceivable
that they can calculate this faster than most people think possible. On the other hand,
if they have passive taps on backbone providers, it's also possible they can just hijack
a session with the click of a mouse.

I don't want to sound like too much of a nut. I've never been terribly concerned about the
government snooping on my data because, well, I'm not doing anything illegal. And aside from
my stance in favor of tighter controls and more electronic freedom, I'm not in many groups
that I think would be targeted. However, I do feel very strongly about what's going on in general
(we already [learned](http://www.marquette.edu/library/archives/Mss/JRM/JRM-main.shtml) that
government records on individuals' activities can be horribly misused). Even more so, I'm
deeply disturbed that *my* personal data and accounts could be compromised simply as a way
for a government employee to gain access to my employer's computer systems, and then to
those of our employees and customers.
