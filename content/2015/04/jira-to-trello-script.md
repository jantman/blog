Title: Jira to Trello Script
Date: 2015-04-10 05:58
Author: Jason Antman
Category: Miscellaneous
Tags: jira, trello, python, ticket, kanban
Slug: jira-to-trello-script
Summary: A script to pull time tracking and dependency information for Jira tickets onto Trello cards.

A few weeks ago, I [posted about](/2015/03/my-new-found-love-of-trello-and-a-helpful-greasemonkey-script/) how I've
started using [Trello](https://trello.com/) to keep track of my work and keep things flowing smoothly. It's been
absolutely wonderful, and I feel more productive and less stressed, and like I have a better idea of what's coming
up. The one thing that Trello is missing is time tracking. I don't need anything fancy, all I really wanted was to
be able to show a time estimate on my cards. I know I could've just put the estimate right in the title of the cards,
but that seemed like a waste of data.

At the moment we're using Jira at work, so I wrote [jira2trello.py](https://github.com/jantman/misc-scripts/blob/master/jira2trello.py).
It's a pretty simple Python script that uses the [trello](https://pypi.python.org/pypi/trello) and
[jira](https://pypi.python.org/pypi/jira) packages from pypi to iterate over all cards on a specified Trello
board, and for each card that matches a configurable regular expression for ticket keys (i.e.
``.*((project1|project2|project3)-\d+):.*``), the script will:

1. Determine if the Jira issue is a subtask, and if so, prefix its title with the issue key of the parent issue,
using the format of ``PARENT-xxx -> CHILD-xxx``.
2. Look up the "Original Estimate" time tracking field in Jira, and if present, prepend it to the title of
the card.
3. Regenerate the title of the card, using the current issue summary from Jira.
4. Move the card to a specified "Done" list if it's closed in Jira.

There are a few assumptions in the script about how the titles of cards are formed, namely that they follow the
``ISSUE-xxx: Summary Here`` format used by my [TrelloContextMenu](https://github.com/jantman/userscripts#trellocontextmenu)
Firefox userscript. But I hope that this might be of use to someone else as well. Please feel free to open issues
or submit pull requests for any improvements that would be helpful, including any assumptions I've made that aren't
valid in your environment. The source can be found on GitHub: [jira2trello.py](https://github.com/jantman/misc-scripts/blob/master/jira2trello.py).
