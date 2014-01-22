Title: Microsoft, Sun, School News
Date: 2007-10-10 00:38
Author: admin
Category: Miscellaneous
Tags: rutgers school iti it microsoft comparison sun solaris java
Slug: microsoft-sun-school-news

Well, I'm currently applying to the [Information Technology and
Informatics (ITI)][] major at Rutgers. I'm in my third year of college
(transferred in from [RIT][] after a trimester there freshman year. This
will also be my fourth prospective major - hopefully this one will
stick. If you're interested in the list, it was a trimester (10 weeks)
at RIT for Fine Art Photography (probably the most fun I ever had in
"school"), followed by the Rutgers list - a semester of general ed
requirements while thinking about Biological Sciences/Pre-Med, then a
realization and a CS major, a year of that and here I am at ITI. CS was
interesting, but it quickly became apparent that the curriculum was far
too low-level to hold my interest - my CS 102 (Intro to OOP / Java) and
103 (Data Structures) classes were interesting, but I kept wanting to
ask my profs why they wanted to fail me for saying that not every
program needs OOP (What? A 20-line shell script is bad because it's a
procedural language?), and couldn't cope with spending weeks on coding a
class to do X when I know that it;s already been done, been GPL'd, and I
could study the code in a night and move on to a program that does
something. The list of higher-level courses didn't look much better.
ITI, on the other hand, has courses in Linux, e-Commerce, and
Information Security, not to mention management-related courses covering
legal aspects, HR, and IS management.

More to the point, we were given an assignment for a research project -
a paper that's supposed to convince the management of an organization
whether or not to adopt a "new" technology. Having a last name between
A-G (I love how professors randomly pick criteria) my assignment is
supposed to be directed towards an online university. We were given a
list of topics to choose from, including social networking sites such as
Second Life, My Space, etc., PIMs, search results visualization (i.e.
Grokker), and a few others. While I guess these are new technologies,
the topic that I chose (obviously not on the list) was "The use of
self-healing technologies in service-oriented organizations". (Yes, I
was hoping that she grades by buzzword count, or at least number of
hyphenated words). I still have almost a week to write the paper, but
I'm hoping to come up with some interesting stuff, including a whole
list of good research references, and lots of talk about LCFG and
cfengine. Stay tuned, maybe I'll end up finding something interesting.
The plus to this whole project is that I realized that as a Rutgers
student, I have access to the entire ACM and IEEE online archives, among
other cool resources.

The Sun Campus Ambassador year is starting to kick into gear. There's a
lot of hype about the new Sun developments such as the unification of
the Storage and Systems groups, the Microsoft deal (grimace), the
upcoming NetBeans 6.0 IDE release, the J2EE and J2ME programming
languages, etc. There's also a lot of boring administrative details,
like remembering to use the names of Sun technologies as adjectives not
nouns (something to do with trademarks that makes no sense to me). This
weekend will be full of organization and Sun training... and hopefully,
plans to take Sun up on the employee discount for Solaris operating
system certification (SCSA/SCNA). Also of interest, I was asked to
complete a survey on the use of Sun technology on campus. I know that a
lot of the programming courses are Java-based, and I'm sure that
NetBeans has a strong following. However, I'm very interested in finding
out how well Solaris has penetrated the University environment (beyond
the fact that every student uses it for Email, Web, Portal, etc. without
knowing it).

**Now, something I wrote yesterday at work:**

After having a Microsoft discussion with someone, I wanted to clear up
a  
few things related to my views on Microsoft. Mainly, that I don't have  
an issue with Microsoft per se. I have issues with Microsoft's
policies,  
and Microsoft happens to be the most publicly visible company with such  
policies. Some of these Include:

1.  The lack of software openness. Both the ethical implications of  
   software that isn't [Free Software][], and  
   functional issues with software that I can't modify to do what I
    want,  
   distribute to others, or (if I were a large corporation) have an  
   independent company audit the source of for security risks. I want  
   control of my software. Microsoft doesn't allow that. Moreover, I
    think  
   that non-technical end users should have the option of having
    control  
   over their software as well.
2.  Software that is designed to a specific intended user, and can't be  
   modified otherwise. Specifically, I'm a technical person. I want  
   software that's designed to be run on a network and an operating
    system  
   that's designed to be administered from a graphical terminal in the
    next  
   room, or over a text-based SSH session from hundreds of miles away.
    If I  
   want to use the command line, I want to have that option. Basically,
    I  
   want options. I don't want someone deciding that I'm too stupid to
    use  
   those options. Other users don't even need to know that a
    command-line  
   is there, but I want to. And, more importantly, I don't believe
    that  
   these options (such as \*good\* remote administration) should
    require  
   expensive server versions.
3.  I want an operating system that recognizes [Free Software][] and
    doesn't attempt to  
   cripple it.
4.  I'm a programmer. I like standards. Things work because of
    standards.  
   We can send e-mail and view web sites because of standards. I think
    that  
   standards are good. And I like \*one\* set of standards which are
    accepted  
   as best. All web browsers let you view web pages via HTTP. I think
    that  
   document formats should have one standard. I think that standard
    should  
   include, for anyone to use however they wish, all of the
    information  
   needed to implement it. I don't want software that goes beyond a  
   standard in undocumented ways. Almost all non-Microsoft browsers
    render  
   HTML in pretty much the same way. Web designers that I know have
    two  
   test systems - IE and not IE. They test their web page under Windows
    in  
   IE to find out how it looks on IE. They test it on anything else to
    see  
   how it looks in everything else.
5.  I don't want a vendor telling me that I have to use their software.
    I  
   don't want someone to tell me that their browser is \*part\* of my  
   operating system. I want to be able to add and remove whatever
    software  
   I want. And I want to be able to make it work. If need be, I want to
    be  
   able to replace software with my own, or with something that I think
    is  
   better. I want to be able to choose what gets installed on my
    computer,  
   in a fine-grained level of accuracy, if I want.
6.  I want proven security. And more importantly, I want to have
    control  
   over the security. I want to be able to add third-party patches
    from  
   organizations like the NSA to harden my security. And I want them
    to  
   pervade every level of the system, not just userspace. I want to be
    able  
   to add security fixes from anyone I want, and have anyone I want
    audit  
   the code.
7.  I want an operating system that's time-tested. I like seeing  
   copyright notices that go back to the 1980s. The fact that an
    operating  
   system has had multiple major redesigns in the past 10 years does
    not  
   speak well for your code. Furthermore, I don't want to buy a
    product  
   that comes in five versions, or however many there are of Windows
    now.  
   I'd be happy with Desktop and Server versions. Maybe even a third  
   Development version. Anything more than that sends me the message
    that  
   you're just trying to tax features and keep them out of the hands of
    users.
8.  I don't want to be locked in to a vendor. Yes, this is a direct  
   reference towards Free/Open Source Software. If your company goes  
   bottom-up, or just decides that you don't care about what I want, I  
   should be able to hire an independent programmer to maintain what
    you  
   gave me, or make the changes that I want. More importantly, if you  
   decide to stop supporting a product that I like, I want to be able
    to  
   have someone else support it, possibly better than you did.
9.  I don't want to buy from a company that actively engages in
    campaigns  
   of FUD (fear, uncertainty, doubt). I want to buy from a company
    that  
   respects their customers/users and their choices. I don't want a
    vendor  
   that engages in scare tactics or buying up competitors and killing
    them  
   off. I want a company that is nice to people. I don't want a
    company  
   that threatens the the customers of their competitors with lawsuits.
10. I want to buy from a company that understands compatibility and  
   strives for it. I don't want a company that tries to bury all
    mention of  
   competing products. I want a vendor that can honestly admit that in  
   certain cases their product X isn't as good as a competitor's
    product Y,  
   but in many other cases it's better. I want a vendor that
    understands  
   that I want to run operating systems W, X, Y, and Z and have them
    all  
   work together, even if this vendor only sells X.
11. A vendor that I buy from will NOT, EVER, tell me tell me that I
    need  
   a state-of-the-art system to run a desktop computer or a server.
    There  
   is no reason at all why my mail server needs to run a GUI. More  
   importantly, in 2007, there is absolutely no reason why my PHP  
   development web server should have 1 Gb of RAM just to run the
    operating  
   system. I'm only coding some HTML form-based apps for a personal
    web  
   site - there's no reason why I need more than 512 Mb to run a simple
    web  
   server. Finally, and this is just a personal thing, but I like a
    vendor  
   that understands students. I'm in college. I want an operating
    system  
   that will install, if not out-of-the-box then with some simple  
   customization, on the type of computer that I'd find at the curb.

  [Information Technology and Informatics (ITI)]: http://www.scils.rutgers.edu/information-technology-and-informatics-major/program-information.html
  [RIT]: http://www.rit.edu
  [Free Software]: http://www.fsf.org
