Title: The Jargon File
Date: 2008-12-12 15:06
Author: admin
Category: Projects
Tags: database, ESR, hacker, jargon, mysql, programming, searching
Slug: the-jargon-file

I know it's been quite a while since I've been around. Hopefully I'll
post more, as the semester is pretty much over and it's time for my
winter projects.

I was pretty bored working on assignments for my [Database
Technologies](http://www.scils.rutgers.edu/component/option,com_courses/task,view/sch,04/cur,547/num,330/Itemid,54/)
class the other day. I had also recently purchased a copy of [*The New
Hacker's Dictionary*](http://catb.org/~esr/jargon/jargbook.html) (the
printed edition of [The Jargon
File](http://catb.org/~esr/jargon/html/index.html)) from
[Amazon](http://www.amazon.com/New-Hackers-Dictionary-3rd/dp/0262680920/ref=pd_bbs_sr_1?ie=UTF8&s=books&qid=1229112625&sr=8-1)
and was reading through it. For those of you who aren't familiar with
The Jargon File, it's the standard glossary of the wonderful terms
thrown around by us geeks and
[hackers](http://catb.org/~esr/jargon/html/H/hacker.html), as well as a
source for definitions of the many words that have fallen out of
favor... well... when people stopped logging in to mainframes to write
their thesi. It's currently at version 4.4.7 and is painstakingly
maintained by [ESR](http://catb.org/~esr/).

Anyway, I happened to be randomly flipping around the book, and landed
on the entry for
[zeroth](http://www.jasonantman.com/jargon/entry.php?id=zeroth) on page
501, which made reference to [fencepost
errors](http://www.jasonantman.com/jargon/entry.php?id=fencepost-error)
on page 187. What a pain to find! So, I stopped by the [listing of
alternate views of the Jargon
File](http://catb.org/~esr/jargon/alternates.html)... but found all of
the ones marked as searchable to be gone. So...

Over the course of a few days (I guess it's an example of how time can
be made - I did this during the final week of the semester, exams and
all, and finished all of my classes as well as this project) I
downloaded the [DocBook](http://en.wikipedia.org/wiki/Docbook) XML,
wrote a few [scripts](http://cvs.jasonantman.com/jargon/) to parse it
out and put it in a MySQL database (complete with cross-references,
indexes, and (hopefully soon) full-text searching).Then, I added a
simple web interface allowing various types of searches and listings.

Though the project was done more to occupy myself and get a little more
experience with PHP parsing XML and doing full-text searches, hopefully
I'll have the time to finish it up - there are still a few minor bugs
(the parsing lost some of the formatting of ASCII art... I think there's
a `trim()` that got stuck in there somewhere) and I'd like to implement
full-text searching of definitions, overall it was a fun project, given
that I did it in about 4 days while working and finishing up school.

If you're looking for a searchable, cross-referenced version of the
Jargon File online (complete with revision history and comments), take a
look at [The Jargon File on
JasonAntman.com](http://www.jasonantman.com/jargon/). There's a [search
function](http://www.jasonantman.com/jargon/search.php), [listing by
first letter](http://www.jasonantman.com/jargon/byLetter.php), [one-page
listing of all
entries](http://www.jasonantman.com/jargon/allentries.php), and
hopefully a few other goodies soon. Most importantly, though the
documentation is sparse right now, the
[scripts](http://cvs.jasonantman.com/jargon/) used to parse the XML,
cleanup the database and display/search everything are available for
anyone who wants them.
