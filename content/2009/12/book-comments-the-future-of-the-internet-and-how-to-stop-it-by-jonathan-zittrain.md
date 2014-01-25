Title: Book Comments: The Future of the Internet and How to Stop It, by Jonathan Zittrain
Date: 2009-12-03 17:34
Author: admin
Category: Miscellaneous
Tags: book, freedom, internet
Slug: book-comments-the-future-of-the-internet-and-how-to-stop-it-by-jonathan-zittrain

Last week I happened to find a Barnes & Noble gift card in my wallet,
with $75 left on it. What a wonderful discovery! One of the pile of
books that I ordered was [The Future of the Internet--And How to Stop
It](http://futureoftheinternet.org/) [by Jonathan
Zittrain](http://futureoftheinternet.org/blog). I'd fully intended to
read the book cover-to-cover, perhaps even digest the content a little,
before throwing my thoughts out there (presumably to get lost into the
vast sea of crap that makes up the "blogosphere"). But I just have to
get some thoughts down on paper...err...LCD.

First off, when I found out that Zittrain is a professor of Internet Law
at Harvard, it immediately told me two things. First, that he probably
sides with content producers and/or Big 'Net a bit too much. Second,
that he probably doesn't really understand what the hell he's talking
about, or why people made the choices they have. The fact that the first
chapter of the book, which talks about history, doesn't seem to mention
ARPAnet once only confirms this. But, the B&N summary sounded like the
book has a healthy dash of iPhone bashing, so I figured it's be a good
read. It was also written in 2008, so I figured that the ideas would be
*relatively current*.

Well, I'm just under a quarter of the way into the book, and given the
vast mass of notes I've penned in the margins, I think Mr/ Zittrain and
I wouldn't get along too well on a desert island. But I'll try to
contain my commentary - and attacks upon the author - until I'm done
with the book. The thought currently in my mind is a very specific one:

> Many technologically savvy people think that bad code is simply a
> Microsoft Windows issue. They believe that the Windows OS and the
> Internet Explorer browser are particularly poorly designed, and that
> "better" counterparts (Linux and MacOS, or the Firefox and Opera
> browsers) can help protect a user. This is not much added protection.
> Not only do these alternative OSes and browsers have their own
> vulnerabilities, but the fundamental problem is that the point of a PC
> - regardless of its OS - is that its users can easily reconfigure it
> to run new software from anywhere.
>
> To be sure, Microsoft Windows has been the target of malware
> infections for years, but this in part reflects Microsoft's dominant
> market share.

Oh, wow, is it 2004 again? I thought we'd given up on the "market share"
argument. When Apache had 10% of the market share of web servers, people
said it wasn't attacked as often because of low market share. Well,
Apache
[currently](http://news.netcraft.com/archives/2009/11/10/november_2009_web_server_survey.html)
has a 47% share of the market, compared to Microsoft's 21%, and it's
still more secure, more stable, and has fewer critical
vulnerabilities\*. The same market share argument was made about Firefox
when it had 5% market share. Now, the share is projected between
[31.85%](http://www.w3counter.com/globalstats.php) and
[47%](http://www.w3schools.com/browsers/browsers_stats.asp), and it
still has less serious vulnerabilities (ones that can actually damage
your computer) than Windows). I thought this "market share" argument was
done with.

Most important is the thing that most Microsoft-biased pundits (and, of
course, Microsoft themselves) don't ever talk about: an amazingly large
number of servers run Linux. Especially e-commerce servers which house
loads of personal information and credit card numbers. Estimates for big
e-commerce sites put non-Windows OSes at 30-50%, and they're quite
popular among small sites that probably don't have well-trained
SysAdmins. So, if Windows wasn't really less secure, wouldn't we see
e-commerce servers getting compromised left and right?

But there's a more important point here. It's about curtailing the
stupidity of users. I know, in Microsoft's defense, that Windows Vista
and Windows 7 are supposed to be better with this. But, at least in the
past, Windows had virtually no privilege separation. With a little code,
you could effect the whole system from an arbitrary binary - or worse,
with ActiveX, through the browser. I was dumbfounded that any user could
install a system-wide application. The real issue here, at least with
older Windows (I don't know much about the new ones) is that Windows,
from the beginning, wasn't written to be secure. Heck, it wasn't even
designed to be attached to a real network.

Linux does have real security advantages over Windows, and not just
because it has low market share. First is an actual, true implementation
of privilege separation. No matter what I do in my desktop web browser,
no matter what I run, even if I installed a Firefox plugin that wanted
to destroy my machine, it couldn't happen. No matter what I let some
random code do, it simply can't escape the confines of my user account.

Ok, ok, I know what you're all saying right now. I can hear it from
here: "but what if the moron does everything as root? what if they just
sudo anything that they're asked about?" Well, I have answers to that,
too. My own distro of choice, [OpenSuSE](http://www.opensuse.org)
greatly upset me when I went to install 11.1, and the installer showed a
default of one user account, automatic login, and the same password for
the user and root. That's just stupid. In fact, it's braindead, plain
and simple. I don't care how wonderful it would be to get Linux on every
desktop in the world, if we have to destroy every advantage that Linux
has over other OSes, it will be worthless.

I digress. In the end, it boils down to user education. And, in some
respects, I think that Linux has become too dumbed-down. There are
certain things that simply shouldn't be put in a GUI. Excuse my elitism,
but if you can't figure out how to configure Apache correctly from the
command line, you have no business running an Apache installation. The
same goes for countless other services and applications. So, what's my
solution? Well, here's what I do when I install Linux for non-technical
friends. Some of these things are training items, others are things that
I do in terms of configuration and, IMHO, should be OS/distro defaults
(unless you know some esoteric hidden switch to change them).

-   Disable graphical login as root. This enforces proper use of sudo,
    and also prevents a user from becoming lazy and operating as root on
    a regular basis.
-   Pick a good, strong root password. Write it down on a post-it note
    and keep it somewhere near the computer. *(Yes, I know what you're
    thinking. But if it's a home computer, anyone already in the house
    either is trusted, or will own the computer one way or another. I'd
    rather have everyone in the house have access to the box, than a
    password that a remote attacker can easily brute force.)*
-   Disable caching of sudo passwords in the desktop manager, if it
    already isn't done. This is a \*very\* bad idea, IMHO, and
    effectively defeats privilege separation. If someone needs to use
    sudo \*that\* often, they're either a knowledgeable user, or they're
    doing something wrong.
-   Set the package manager to use the strictest key verification
    settings.
-   Provide the user with extensive documentation (can be a list of
    links to helpful sites) that includes - *this is of paramount
    importance* - a list of common Windows (or whatever OS they're
    coming from) programs and their closest Linux equivalents. This is
    another measure to try and dissuade the user from searching for and
    installing arbitrary code.
-   Give the user a good, simple explanation of what sudo is, what root
    is, and why they should be worried. One of my analogies - if I have
    time to explain it - is to think of the computer's security like a
    jewlery store. Your user account is the front door; only people who
    look honest are buzzed in, but they still can't do much damage. The
    root password is the combination to the vault; only very trusted
    people can get in, and they only open it when they absolutely have
    to.
-   Enable a wide range of trusted repositories by default. The more
    likely the user is to find a package in the repos already cached,
    the less likely they are to download arbitrary code.
-   Explain to the user that when you install software (as root), you're
    essentially giving the developer access to your system. Software
    should be screened by someone who knows what they're doing (i.e. the
    community) before you install it.
-   I always tell people to \*only\* install software from the
    repositories I enable. If there's something they need and it isn't
    available, ask me (or ask the community) and I'll make a package and
    upload it to a suitable repository. The key here - and the most
    difficult part - is to conquer the Windows habit of installing
    software from disparate sources, and train the user that only
    software from their repositories, or other community-standard
    repositories, can be trusted.
-   Show the user the correct patch/update procedure for their system.
    Depending on skill level and the level of attention you're willing
    to give them, it might be advisable to enable automatic updates (if
    the OS doesn't have a way to do it, then via cron).
-   If the user is a developer or needs to run any services, even just
    for development - i.e. Apache, MySQL, Postfix, etc. - properly
    secure them and give an overview *and* links to the proper security
    procedures.
-   Setup a second user account. Explain to the user that this is *only*
    to be used for banking and other sensitive activities. Lock it down,
    make sure it's in a different group from the main user, don't
    install any Firefox plugins.

Unfotunately, a *lot* of this is just breaking the bad administration
and security habits shared by most Windows users.

While we're on the topic, a word about package managers. I'm a Linux
sysadmin, and I believe in 'eating your own dog food'. I've used Linux
on all of my servers, desktops, and laptops for over 4 years now. I
haven't used Windows on a regular basis in ages. I'd say I touch a
Windows box for about 5 minutes a month, and usually just to use a
browser. A few weeks ago, I was asked to install Windows on a desktop
for someone. I did. I then attempted to install Firefox. Using what I
remembered of Windows, I navigated to the "Control Panel" and clicked
(err... double clicked) on "Add and Remove Programs". Seems logical
enough. I then stared at the screen for about 30 seconds, trying to find
the Search box, where I could type in "Firefox". Finally, I literally
began laughing out loud, when I remembered that Windows doesn't have
unified package management, and I'd need to manually find the Firefox
binary on their web site, download it, and run whatever installer
program Firefox chooses to use. Same issue with updating software. I'm
utterly perplexed, being a Linux user, that Windows and Mac people still
search through Google or multiple web sites just to find new software.
I'm even more perplexed that the OS update/patch program doesn't also
update all of the software on the system. It seems like the stone ages.

In my opinion, one of the biggest failings of modern Linux package
management is the assumption (derived from multi-user systems) that all
software should be installed system-wide. Granted, it doesn't do a whole
lot to actually protect a single user if they install malicious software
available to just themselves (especially since most desktop installs
these days are probably used as single-user systems), but I really feel
that distros (especially desktop-oriented distros) should have an option
to easily install packages for just the current user, and possibly do
this by default.

\* I can't find the link right now, but I did find an interesting
article on Microsoft's old anti-Linux campaign ("get the facts"). One of
the things mentioned was that when Microsoft compared "vulnerability
counts", they were actually comparing: 1) entire Linux distros vs just
the core Windows OS, and 2) counting individual patches in Linux versus
patch sets released by MS. So, not only was MS literally counting apples
and oranges, but they were totally ignoring unfixed vulnerabilities.
Given Microsoft's habit of not fixing vulnerabilities - especially in
"unsupported" products - it's no wonder how they got the numbers to look
so good.

</p>
So, here's a thought. People are used to paying for an OS and for
software. Start a Linux vendor that sells a desktop, newbie-oriented
Linux distro. Charge a per-user flat rate for the distro and a bunch of
base packages, that includes X hours of telephone support. Charge per
hour/minute/whatever for additional support. Bundle in secure VNC,
secure remote access, etc. in a way that will allow support to remotely
access the computer, but preserve the privacy and security of the user
(perhaps an app that allows the user to initiate a reverse VNC or SSH
session to support). Lock down root access - allow the user to do it,
but remind them every time that, outside of a specified set of commands,
their actions will be logged and won't get full support. Then figure out
a way for support to write a shell script that's sent to the user to
perform administrative actions, which will all be listed in relatively
simple terms for the user to examine and approve. Finally, have a
\*giant\* package repo, all of which is free or comes with paid support.
Any F/OSS packages that aren't already in the repo can be requested by a
customer, and for a flat fee for the first requesting customer (say,
$10) will be examined, approved, packaged, and added to the repo.
