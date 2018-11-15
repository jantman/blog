Title: Please Don't resize my browser
Date: 2009-06-22 23:48
Author: admin
Category: Miscellaneous
Tags: design, standards, web
Slug: please-dont-resize-my-browser

It always amazes me to see how much "old school" web design practice is
still out there. I'm talking about commercial sites (not MySpace pages)
that blatantly ignore web standards about both content and user
experience. This isn't just a Linux thing, though some aspect of it
certainly is. The web site of my home town,
[mpnj.com](http://www.mpnj.com) uses a Flash-based navigation menu that
even the official, proprietary Flash player for Linux won't support -
the transparency renders as white, obscuring the text beneath the fully
extended size of the menu. I emailed the developer about this on the
launch day, and was told in no uncertain terms that - despite the fact
that he had a fully-functional alternate version - Linux wasn't
important enough to fix the site. Ironically for a town government web
page, it also doesn't incorporate any accessibility features, which
seems to be standard for most of these poor designs.

There are still countless large news sites whose Flash-based video
players won't run under Linux, and even CitiBank's credit card site has
a flash ad that plays incorrectly under Linux.

The real pain that I happened to see today was a company who uses
coupons.com to allow customers to print out retail coupons. My first
surprise was that to print the coupons, you have to download Windows or
Mac software. I'm not quite sure how many people will do this, but it's
probably how viruses spread so quickly (people who will download
anything that claims to get them half a dollar off of a roll of toilet
paper, or whatever the coupons are for). So, that's not cool - most
coupons I've gotten were just HTML emails or PDFs. If their thinking is
to control the distribution (they make some comment about a "paper-based
printer, not a fax or PDF creator"), they've obviously forgotten about
photocopy machines and scanners, let alone capturing the spool file on
Mac.

More striking, however, was the shock of opening their help page. My
primary monitor is a 24" widescreen, and I generally keep a browser
window occupying half the screen width and a terminal next to it. Once I
opened their "help" site, it promptly resized my browser window to a
tiny 640x480!

This problem, unfortunately, isn't as rare as it should be. There are
still sites that force browser size, disable right clicks (I hadn't seen
that since about 2004 until a few weeks ago... obviously someone who's
never used \`wget\`) or have a page that doesn't fully work in FireFox
on any platform. Even worse, my personal pet peeve (as at the time of
writing this I have about 50+ tabs open in Firefox, and it's only using
a small sliver of my 2GB RAM) is sites that don't play well with tabbed
browsing - either using only JavaScript for *all* navigation links, or
opening all links (site-wide) in the same tab/window. I don't know how
many web sites have lost my business because of this. Or the one I know
of that starts a new shopping cart for every tab opened (so if I open
each product I want to buy in a new tab, when I add them all to the
cart, it ends up with only one).

I don't know how there can be anyone out there who's still not using
valid XHTML with all of the accessibility features for anything new,
especially a commercial site. But even more so, how can there still be
people designing web sites who disregard the golden rule of web design:
**Don't mess with someone's browser.** Leave things like where to open
the link and how big to make the browser to the user. If they're not
technically literate, changing what "usually happens" will just confuse
them. If they're well-versed in how to use a web browser, like me,
they'll just get aggravated by having someone else change their workflow
(I doubt the guys who designed those sites would like it if I told them
they had to design the whole thing in Emacs). If they're somewhere in
the middle (just found Ctrl+click in Firefox), you'll confuse them. And
God forbid they're blind and using a page reader... good luck with
JavaScript or Flash navigation.
