Title: A Rant on Post-Secondary Tech Education
Date: 2015-10-05 16:46
Author: Jason Antman
Category: Miscellaneous
Tags: college, computer science, CS, technology, education
Slug: a-rant-on-post-secondary-tech-education
Summary: A rant on the state of post-secondary technology education.

*(Disclaimer: First, I know there's a wide range of curricula in the CS/tech education world,
and some schools are better than others; there are certainly programs that prepare students
much better than what I experienced. Second, these views are somewhat biased to my own
experience in the web, agile and DevOps worlds; for people who want to write Java for banks
their whole career, I'm sure most schools prepare them well.)*

It's been a decade since I've been in the University system, but I've seen precious little to
indicate that much has changed since then. I graduated with a degree in [Information Technology
and Informatics (ITI)](https://comminfo.rutgers.edu/component/cur,547/option,com_courses/sch,04/task,listing/);
I switched majors partly because of my deep hatred for calculus, and partly
because I was already working for Rutgers University as a student systems programmer, and it
was painfully obvious how little the CS program would do to prepare me for a career. My time
in CS was spent writing pitifully small Java applications in teams as large as **three** (any
team work was highly unusual) and playing with linked lists. I switched to ITI so I could take
classes on IT management and policy, information security and "web application development" (with
databases and JSON!) Since then, I've had two family members enter CS or ECE programs, and I
tried to give them the best advice I could. I happened to be thinking about it, and figured
I'd write down some of my thoughts.

First and foremost, I understand that technology changes very quickly - a lot quicker than
college syllabi. However, my alma mater's [undergrad course list](https://www.cs.rutgers.edu/undergraduate/courses/)
does not appear to have changed _at all_ since I took some of those classes a decade ago.
Don't get me wrong, it's very good that we're teaching classes in Operating Systems Design
and Compilers. But current curricula seem to focus almost exclusively on fundamentals
and low-level details. When I was in college, almost all the classes were taught in Java,
and that already seemed dated and ignoring the "Web 2.0" world; these days, it relegates
most graduates to jobs that I'd consider boring, in the Enterprise sector. Rutgers' undergrad
CS catalog doesn't list "Internet Technology" until CS 352, and I'd be surprised if any
networking (aside from maybe "use raw sockets to do something") is covered before that class,
which is tentatively designed for third-year students. Very few of the courses that I see
listed (and many that I looked at haven't changed their description, or even their instructor,
in ten years) do much to prepare students for the actual tech industry. Even worse, most
of them are the same classes that I found boring, and caused me to switch majors.

Obviously, I can understand the argument that tech moves too fast for class materials
to keep pace. But introducing the Internet as a third-year topic, and Distributed
Systems as a senior-level class? Writing *everything* in Java? This seemed silly
to me a decade ago; now, it seems downright wrong for a department that claims to
prepare students for careers in technology. Once again, I agree that a strong grasp
of fundamentals is overwhelmingly important. However, a balance needs to be struck
between this and (1) providing students with useful, current skills, and (2) keeping
students interested. In a world where more and more (and in many areas, such as my own
subculture, almost all) software runs in the browser, how can education ignore this?

I'll take a small moment to dovetail this to a heated topic in tech at the moment:
hiring practices and diversity. The tech education at most universities does little
to prepare students for actual jobs outside of, quite literally, "entry-level Java
programmer". The people who will get good, interesting jobs in tech (yes, that's quite
opinionated; I'm defining that as jobs with web or DevOps shops) are the ones who
either have ample free time and pre-existing interest to hack on their own projects,
and/or are insomniacs and can handle going to class, working, and still writing
a lot of code and experimenting on their own. I suppose this ends up being biased
towards stereotypical white males, even if only because it seems socially acceptable
for us to ignore having a social life in favor of finishing those last lines of code.

But I digress. There are few other industries that I can think of - and certainly
no professions - where someone leaves the University system with the highest
degree commonly attained in their field, yet has virtually zero real world
hands-on experience. I'll leave out the doctor or lawyer analogies, but some
of our closest parallels - engineers, architects, etc. - graduate and are able
to start practicing their profession. Sure, there's organization- or domain-specific
on the job training, but for the most part, they can do what they were hired to do.
On the other hand, tech-focused programs are turning out graduates many of whom
have never seen the tools (or even languages) that we use. They don't have
any real experience working in teams larger than three or four (at the best),
and have no concept of what goes into developing real software, working in
a large (or distributed) team, or what happens to software after someone
grades it (which in my experience, was usually as simple as "does this program
produce the right output when it's run at the command line).

So, that's my rant. What do I think should be covered in tech/CS curricula that isn't?
Here are a few:

* __Testing__ - I have painful memories of being marked as failing assignments because
I used a tab when the instructors expected some number of spaces in the output of my
program. In most cases, my instructors used a test harness that exec'ed our Java applications
and inspected the string output. I still have no idea why they didn't use JUnit. But that's
beyond the point; we're turning out programmers who don't know what unit or integration tests
are. I still don't understand how I got through a four-year degree, partially in CS and
partially in IT, without writing a single test for any program I wrote (aside from a few
courses where we wrote "test harnesses", but never used a proper testing framework).

* __Software Distribution__ - Here's another no-brainer. Why - especially when working in
Java - would students email completed assignments to professors, or upload them to online
courseware, when so many artifact repositories exist? If people can't use your software it's
pretty pointless. Distribution should be a part of at least some assignments, whether it's
an open source model or just uploading an artifact to an internal maven repository.

* __Maintenance__ - Ok, sure, this is the part that none of us really like. But it's also
an inherent part of what we do, and the odds are most entry-level programmers will first
find themselves fixing bugs or adding features to someone else's application. Being able
to read and understand existing code is perhaps the most important thing we do, whether it's
to fix it or just to learn from it. Nobody I've talked to about education as a programmer
has ever encountered an assignment of "here's an application, here's a bug report, find and
fix it" beyond the most trivial contrived examples. The process of fixing a bug in or adding
a feature to an existing codebase is probably one of the most important lessons in learning
to write code - even if it's partially a lesson in what not to do.

* __Distributed Projects__ - _The_ "big" project in my time as a student was pairing on a Java
GUI/backend program. Perhaps I didn't have the best experience, as my partner neglected to write
any code. However, few people are going to enter the workforce and be the sole person touching
a given codebase. I think there should be much more emphasis on working as part of a realistically-sized
team. Sure, the tooling might not be the same, but at least graduates should have some experience
in collaborating with others, and more importantly, in working on code where they don't necessarily
understand all of it. If we're going to teach Java, we should at least be teaching it realistically
and throwing in some black-box classes or having students code to each others' (not-yet-complete)
APIs.

* __Web-First__ - With the plummeting cost of cloud computing and containers, and the massive
compute farms available at most universities, there's really no excuse for completely ignoring
the Internet. Sure, it doesn't play much of a role in the low-level basics, but for the classic
"hello world", calculator app, tic-tack-toe, etc. it's not really that much overhead to do
them in [Spring](http://spring.io/guides/gs/rest-service/) or [Flask](http://flask.pocoo.org/)
or [Rails](http://guides.rubyonrails.org/getting_started.html) and also give students exposure
to a modern, web-centric framework that someone might actually use to write a simple application.
Most programmers are probably going to touch the web at some point. I'd argue that it's also a
lot more applicable for people who aren't going into a distinctly programming role.

* __Operable Software__ - Going with the web-first paradigm, we have the virtualization or
container technology to give students a shell and a running web server. Why not show them
how to use it? I once failed a major assignment because the graders used a script that combined
STDOUT and STDERR and evaluated it. They asked me what all these weird lines in my output
were; I told them it was log4j. They asked what that was. Even the classes I took that
included working in teams or something else somewhat realistic, completely ignored the
operations side of software, as far as never discussing logging. If we want the quality
of software that we (as an industry) turn out to increase, one of the best things we can
do is introduce programmers to logging, testing, debugging and the operations side as early
as possible, even if in a quick, superficial way. If students had to actually _run_ their
app, and let it serve actual requests, they'd have a lot clearer picture of what software
actually does after the build a JAR. Related to this, an introduction to the concepts
of security and stability would be quite useful.

If you're currently going to school for something programming-related, here are a few
things that I'd recommend doing to get ahead of the pack:

* Learn some languages. Look through job ads for the type of entry-level/graduate work you
hope to get when you graduate, and see what they're asking for. If your school is still the
way mine appears to be, in a CS program you'll probably be exposed to Java and C. Learn some
Ruby or Python, or something else that's in use on the web. It certainly won't hurt you, and
it'll also be less intimidating to learn a new language once you already know a few, preferably
that are rather different.
* If you want to work in the web world and are a Windows person, learn Linux. Despite what
some people tell you, it's the rule not the exception.
* Read. I understand that not everyone has extensive time to experiment on their own, and I know
a lot of people who didn't, especially in college. Read. A lot. It seems that most tech programs
require a lot less work than other engineering disciplines; I remember how envious my ECE and Mech-E
friends were at the "low" amount of work we CS/IT majors had to do. Read everything you can, especially
about the industry you want to work in (if you have an idea of what it is). Find out what tools they're
using from job ads or company tech blogs, and find out about them. Even if you can't use them
yourself, at least knowing a bit about them will help a lot.
* If you can, find an open source project or two to work on. This one comes with a bit of a warning;
the open source world can be quite abrasive, and sometimes downright hurtful. Unfortunately, technology
as a whole seems to attract a lot of very loud, angry, bad people. So do some research; try to find
a project that you're interested in and that you have some relevant experience for. But most importantly,
find a project that's clearly open to mentoring new contributors; they're unfortunately few and
far between, but it will really pay off.
