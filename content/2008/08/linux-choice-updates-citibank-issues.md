Title: Linux, Choice, Updates, CitiBank issues
Date: 2008-08-25 12:37
Author: admin
Category: Miscellaneous
Tags: citibank, citicards, firefox, flash, linux
Slug: linux-choice-updates-citibank-issues

**Update July 11, 2011** - I [just found
out](/2011/07/article-on-theinquirer-net/) that this post is heavily
quote in [an article on
theinquirer.net](http://www.theinquirer.net/inquirer/news/1026958/citibank-infuriating-customers-linux-hostile-site)
about this issue. Luckily (I don't know whether I made a difference or
not, certainly CitiBank never contacted me back), citicards.com now
works with Firefox on Linux. I have no idea if it was a change made by
Citi, or a change with Firefox or Flash Player.

I know this blog has been less-than-active lately. Life has been pretty
busy, between a massive network upgrade at the [ambulance
corps](http://www.midlandparkambulance.com) that I volunteer with, the
impending doom of a new semester at work, scheduling courses, and a few
personal projects. I do, however, have a long list of things to post,
including some notes on my upgrade to [Nagios 3](http://www.nagios.org),
my recent experience with the [PC Engines
ALIX](http://www.pcengines.ch/alix.htm) board, some changes to
[tuxOstat](http://tuxostat.jasonantman.com), and my plans to upgrade to
Optimum Business cable with 5 static IPs - finally a real home for
[JasonAntman.com](http://www.jasonantman.com).

**CitiCards Problems -** I had a somewhat unnerving experience this
morning. Having just gotten a Citibank credit card, and made my first
few purchases on it, I browsed to
[CitiCards.com](https://www.citicards.com) to check my account summary.
I happened to be using a just-purchased IBM T41 laptop, running
[OpenSuSE 11.0](http://www.opensuse.org) and
[FireFox3](http://www.getfirefox.com), so when I saw the page display
and then go completely blank, I suspected a problem with my Flash
plugin. Little did I know, but I tried the same page on 3 other
Linux/Firefox machines, with the same result. I put in a call to the
tech support line, and was gruffly informed by the representative that
Firefox was not supported, they were unable to support it, and, to
paraphrase, I should get another browser or f\*\*\* off. She was *very
well-aware* of the issue, and stated that Citi would not fix it. At this
point, I stated that I thought I would cancel my card, and she told me
to have a nice day and hung up.

I decided to go to [step 2 of the Generic Problem Solving
Method](http://www.jasonantman.com/wiki/index.php/Generic_Problem_Solving_Method),
and found [hundreds of references to a problem with CitiCards.com on
Linux](http://www.google.com/search?hl=en&q=citicards.com+linux&btnG=Google+Search).
I read through a lot of conspiracy theory, but decided to test one of
the theories (and fixes). Sure enough, when I right-clicked on the blank
white screen, I got a Flash context menu. Clicking "Play" showed the ad,
and I was able to click the little "X" in the top right and bypass it,
gaining access to the normal main page. Never to be one to ignore a
conspiracy (or anti-Linux) theory, I pulled up the same page on a Mac.
Sure enough, that particular ad (set not to play and with an opaque
full-screen background) didn't show up. Hmm... maybe there's something
to the theory put forth by the [guy who said CitiBank is blocking Linux
users](http://stealcode.blogspot.com/2008/07/citibank-doesnt-like-linuxubuntu_27.html).

I decided to call back, and this time spoke with Susan at CitiCards tech
support. She was very understanding, and apologized for both the
inconvenience and the previous representative's attitude. She said that
she was aware of some issues with Firefox and Linux, but stated that
they are only unsupported so far as Tech Support won't walk a customer
using Linux or FireFox through any issue resolution, but that both the
browser and architecture should, theoretically, work. She didn't know
anything about a policy against Linux, or intentional blocking/sabotage.
She did say, however, that they are "working on it". I did inform her
that the problem could probably be resolved by simply editing the Flash
ad to be properly transparent, or suppressing it for Linux
architectures, though I doubt that the information will make its' way up
the food chain. Unfortunately, I can't seem to find a contact email for
anything site-related on CitiCards.com.

If this is really a case of intentional blocking, it would be quite
infuriating - I filled out the application for the card on
FireFox3/Linux... but then they block account access?

Hopefully more of an update tonight...
