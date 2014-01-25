Title: Print Accounting
Date: 2007-11-27 00:51
Author: admin
Category: Projects
Slug: print-accounting

Since we moved into our apartment at the end of last summer, my
roommates and I have had a Brother 5170DN monochrome laser in the
hallway as a communal printer. Last weekend, two new printers arrived -
I got a Xerox DocuPrint N4525 - a big surplus student lab printer that
handles paper up to 11x17" and print rates of up to 45 PPM. My roommates
picked up a (free!) HP Color LaserJet 4500. So, I decided that I want
accounting of who prints what on each printer.

I setup a Dell PowerEdge 650 running openSuSE 10.3, Xen and 2 NICs, one
on our main network and one with a static IP in a separate subnet hooked
up to a small 5-port switch. I setup a Xen VM (also openSuSE 10.3) to
act as a CUPS server. I then installed
[tea4cups](http://www.pykota.com/software/tea4cups) which allows
outgoing CUPS jobs to be read via a pseudo-backend while they're
processing. tea4cups calls some PHP scripts that update a MySQL database
with job information, including page counts and ink coverage amounts
calculated by [pkpgcounter](http://www.pykota.com/software/pkpgcounter).

This is all done with a kludge of custom scripts, which I'll put in my
CVS repo (and comment on here) sometime this week.

I did run into two problems. First, I had issues with getting tea4cups
to run at all. After googling a bit, I read about people having problems
with tea4cups and SELinux. Sure enough, I disabled AppArmor and all went
back to normal. Also, I later had some problems trying to perform ink
accounting on a color printer. After some investigation, I also found
out that GhostScript 8.15 is buggy and will cause problems with
pkpgcounter. I upgraded to the 8.60 RPMs and all was well.

The whole project is still in the works, but when finished I should have
a system that will keep track of all printing in the apartment by
username and IP, and track the page count, paper size, color or B&W,
resolution, and ink coverage percentage (both for grayscale and CMYK or
RGB individually). I know it's overkill - all I want to really know is
enough data to fairly split the costs of paper, toner, etc. - but I
thought it would be a fun project.

I originally thought about using
[PyKota](http://www.pykota.com/software/pykota) for the accounting, but
found it to be way too heavy-weight. My current kludge, done up in one
night (before writing an essay), is based on CUPS and tea4cups, which
calls PHP backend prehooks and posthooks, which in turn make use of a
few pre-written python and perl scripts that deal with querying
information from the printer (IPP) and local files.

All in all, for something that didn't exist 24 hours ago, I think it's
working pretty well so far.
