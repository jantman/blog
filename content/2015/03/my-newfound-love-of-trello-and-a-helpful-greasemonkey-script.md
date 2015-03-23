Title: My New-found Love of Trello and a Helpful GreaseMonkey Script
Date: 2015-03-22 19:36
Author: Jason Antman
Category: Tech HowTos
Tags: Trello, kanban, tickets, organization, work
Slug: my-new-found-love-of-trello-and-a-helpful-greasemonkey-script
Summary: How Trello has made my past week so much less stressful, and a helpful GreaseMonkey script to help add new cards.

When I started at my current job two and a half years ago, we were just really getting into [Kanban](http://en.wikipedia.org/wiki/Kanban_%28development%29).
We used a web-based Kanban board ([Kardboard](https://github.com/cmheisel/kardboard), written by our director of development at the time), and each team had
their daily stand-up status meetings in the middle of the office in front of a projector screen, with their board filling the entire wall (and remotes on Skype). It took me a while
to get used to it, having always worked in very ticket-and-emergency-driven ops roles. But once it clicked, it was like an epiphany. Suddenly I could see all
of the (non-breakfix or unforeseen) work headed to our team, its priority and due dates, and what everyone (including myself) was working on at a given moment.
Even though work-in-progress (WIP) limits never made it to the ops team, it reduced my stress level amazingly. Instead of dealing with a massive queue of tickets
assigned to me - some of which were such low priority I'd probably never get around to them - suddenly all I had to concern myself with was my WIP and what was
next up for me.

Over the past year we've had a major (almost complete) changeover of management, and many of the old ways have disappeared. Some might even say that, as a technical
company, we've regressed quite a bit. Either way, we haven't been using Kanban for over six months. Our development teams are moving to [Scrum](http://en.wikipedia.org/wiki/Scrum_%28software_development%29),
and our more ops-y teams (I'm now on our Automation and Tooling team, straddling the awkward line between the two) are trying to figure out what's right for us.
And I haven't been this stressed since I started work here; my team is both busier than ever and understaffed by almost 50%. We stopped using the Kanban board in our
stand-ups, our new manager stopped referring to it, so (even with mostly-working synchronization with Jira) it stopped being useful, and I stopped using it. Without thinking,
I went back to my old "page showing <em>everything</em> assigned to me" view in our ticketing system, and grew increasingly frustrated by managing my WIP and deciding what
needed to be worked next.

So, after discussing this with the rest of my team, last week two of us came to the same conclusion, independently, on the same day: use [Trello](https://trello.com/) to
run our own personal Kanban boards. I've been doing so for about a week now, and all I'm horribly embarrassed that I didn't think of this sooner. It's absolutely wonderful -
I can keep managing my own work in a Kanban-like form (albeit without formal WIP limits) without needing management endorsement. Sure, it only works for things that I know
are coming and takes some manual curation time, but so far, it's been amazingly refreshing and calming. The best part is being able to (once again) visually see
both my WIP, and my recently-complete work.

Someone else on my team mentioned that they use Trello for their personal tasks; I created two more boards, one for my personal development work, and another for my general
around-the-house tasks and to-do's (my wife connected with her inner manager once I shared my board with her and she figured out that she could re-order by backlog...).
It's 8 PM on Sunday night, and I can confidently say that I've had one of the most productive weekends in ages. And one of the most relaxing. Instead of spending
lots of time trying to figure out what I have to do this weekend and what the priorities are, I just used the same Kanban method that I loved from work. And it
paid off.

## The GreaseMonkey Script

The one thing that initially bothered me about Trello was the time it took to add cards. At work every task I have is in either our ticketing system or
a GitHub Issue. Our previous official tool, [Kardboard](https://github.com/cmheisel/kardboard), synchronized with Jira so everything was always
up-to-date and on the right board. At first I was adding cards manually, but I figured there had to be a better way. A quick Google search turned up
a [Bookmarklet](https://github.com/danlec/Trello-Bookmarklet) by [Daniel LeCheminant](https://github.com/danlec) of Trello, to add a Trello card for the current
page. It does some really cool stuff, like parsing Jira and GitHub issues and setting the card title nicely for them, as well as some other ticketing
systems. I also found a [GreaseMonkey script](https://gist.github.com/aggieben/5811685) from [Benjamin Collins](https://github.com/aggieben) of StackExchange
that adds a link to create Trello cards from StackExchange meta posts.

So, I took things a bit further and whipped up a GreaseMonkey script, [TrelloContextMenu](https://github.com/jantman/userscripts#trellocontextmenu). It
uses Daniel's card naming code (plus fixing the GitHub format a bit and adding support for [ReviewBoard](https://www.reviewboard.org/) code reviews) and
the GreaseMonkey/Trello logic from Benjamin's script. Once installed and authenticated with Trello, the script retrieves a list of all of your boards
and cards, and adds an "Add to Trello" right-click context menu in Firefox, allowing you to add the current page to any list on any of your boards.

[![screenshot of TrelloContextMenu context menu popup in Firefox](/GFX/TrelloContextMenu_sm.png)](/GFX/TrelloContextMenu_large.png)

The script is [available on GitHub](https://github.com/jantman/userscripts#trellocontextmenu) (the link in the README will go to an installable raw
version of the script), and uses GreaseMonkey's versioning capabilities. At the moment I've only tested it with GreaseMonkey in Firefox, and I don't
expect it to work elsewhere as it uses a few GreaseMonkey-specific features, such as ``GM_xmlhttpRequest`` and GreaseMoneky's browser-wide SQLite
persistent storage (to store your boards and lists, and authentication credentials, until you manually refresh). I'd be happy to accept pull requests
from anyone who can get it working in other browsers.
