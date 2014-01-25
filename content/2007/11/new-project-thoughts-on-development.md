Title: New Project, Thoughts on Development
Date: 2007-11-19 23:49
Author: admin
Category: Projects
Slug: new-project-thoughts-on-development

I know I don't update anywhere near often enough - then again, I update
a lot more here than I do on my Sun blog. But I'll do better, I promise
- and I'll setup a new template, too. Maybe tonight.

So I was just thinking about my software development - about how many
projects that I never finished, or never even started. And it got me
thinking. When Rutgers laid off all of us part-time programmers and I
was given a few choices for a new job, I chose tech support for student
labs and classroom connectivity. Why? Obviously I'm not going to learn
much. But I like putting out fires. I like solving problems. More
importantly, and more of an issue when I try to write software, I like
meeting a list of minimum requirements and just doing that. I love
solving problems and I love making things work. On the other hand, at
least when it comes to open-source (and no-cost/no-pay) projects, I have
serious problems with motivation. Or, should I say, I get a project to
do what I need, and I abandon it.

I guess I should print some sort of warning on my project pages. Or, I
should be happy that F/OSS is getting as popular as it is. Even among
people who don't know what it's about. I've been getting endless emails
about my [PHP EMS Tools.](http://www.php-ems-tools.com) I've marked it
as beta. The readme and the extensive docs make it clear that it's not a
finished work that's suitable for everyone. I make it clear that I don't
do tech support for Windows, as I know nothing about it. Yet, it seems
that finding a project on SourceForge or Google is wonderfully easy, yet
it's easier to just e-mail the developer than take the time to read the
docs. I mus say, though, that when I download something on SourceForge,
especially something that isn't marked with a complete/stable status, I
fully expect to spend a few hours playing with the source before getting
it up and running.

Anyway, I don't look at my lack of follow-through as a horrible thing. I
have a problem. There's nothing else out there that even begins to solve
it. So, I write something that solves my problem. The next time someone
has the problem, they can use my code. If I didn't carry it far enough,
they can pick up where I left off. When they get it where they want it,
they can send their changes back to me.

Lately, I've been reading a great book - "[Hackers: Heros of the
Computer
Revolution](http://search.barnesandnoble.com/booksearch/isbnInquiry.asp?z=y&EAN=9780141000510&itm=1)"
by Steven Levy. There's some really great reading about the good 'ol
days at the MIT AI lab, and the Homebrew Computer Club and the
beginnings of PC's (the Altair). And there's a lot of commentary about
[The Hacker Ethic](http://en.wikipedia.org/wiki/Hacker_ethic) - a
definite forerunner to the Free Software/Open Source movement. Most
specifically, the idea of software belonging to the people, of source
code being open and freely distributed for the good of everyone. And it
really gets me thinking. People sometimes ask me why I don't sell the
software I write. Why should I? I'm not writing it for a client, I'm not
getting paid to write it. I'm writing it for me. It seems \*wrong\* not
to let others benefit from my work. And even if I was writing it for a
client, why not give it away to others? Many people might not, but I'd
give paying clients a break if they agreed to GPL the code.

Anyway, for a while I've been trying to find software that will run on
Linux to draw network maps. The networks at my house and apartment have
gotten complex enough that it's hard to hold everything in my mind. I
made an attempt to draw a map in Dia and Kivio, but they just didn't cut
it - all of that manual updating. So I wrote a little PHP script that
uses Imagick (the PHP wrapper to ImageMagick) to generate network maps.
It takes a simple XML files, one per host, to define devices and
connections. It outputs a nice PNG map, defaulting to 800x800 pixels,
but can be scaled up large enough to print on a 36" wide plotter. Code
can be accessed through CVS
[here](http://cvs.jasonantman.com/cgi-bin/viewvc.cgi/cvs/misc-scripts/networkMap/).
It's not an official release so the docs aren't complete, but there are
ample comments in the code and sample config files. Most importantly,
it's all wraped up in one PHP function, so generating a map (once you've
generated XML config files) is as simple as including a PHP file and
calling one
function.
