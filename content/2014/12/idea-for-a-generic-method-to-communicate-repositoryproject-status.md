Title: Idea for a Generic Method to Communicate Repository/Project Status
Date: 2014-12-07 18:24
Author: Jason Antman
Category: Miscellaneous
Tags: repository, project, git, github
Slug: idea-for-a-generic-method-to-communicate-repositoryproject-status
Summary: Some ideas for generic methods of communicating the status of a project / source code repository to humans and machines.

First, something funny, before my possibly-hair-brained scheme:

[![commitstrip.com "side project" comic strip](http://www.commitstrip.com/wp-content/uploads/2014/11/Strip-Side-project-650-finalenglish.jpg)](http://www.commitstrip.com/en/2014/11/25/west-side-project-story/)

I know I'm not alone in having a mess of [repositories on GitHub](https://github.com/jantman?tab=repositories); I personally have over 90, and they're
all in various states of "doneness." Some are working and undergoing active development. Some should be
working, but I no longer use them (and sometimes lack "things" needed to use them, especially the case
with projects linked to specific hardware). Some of them were ideas that never took off; some of these
I intend on finishing, and some I never want to touch again.

While GitHub has a [Releases](https://help.github.com/articles/about-releases/) feature, at best (where everyone
understands and follows [semantic versioning](http://semver.org/)), it can only differentiate "initial development"
(prior to stable public release) versions from those after them. It may be an indication of the usability or completeness
of the software, but not of its current state of maintenance.

The questions that I'd really like to be able to answer about a given project or repository are:

* What is the "completeness" of the code? Should it be usable, or is it functionally incomplete?
* What is the status of development efforts? Is this actively developed, or supported (even if bugfix-only), or totally abandoned?

I'd like to be able to easily communicate this to people who come across my work, and also
track it for my own needs - I have enough repositories with barely-started concepts that I
occasionally forget about them. I'd also, of course, like to be able to know this information
about other peoples' work as well.

Ideally, I thought that this should be a GitHub feature, exposed via the API and the UI. However,
there are a number of problems with that:

1. It would require GitHub to implement the feature. Quite ironically, GitHub is [not very open](https://github.com/isaacs/github/issues/6)
about issues and feature requests for their platform itself, and the only good way to suggest something is [unofficial](https://github.com/isaacs/github).
2. It would be tied to GitHub directly. When the next big thing comes along, or for projects using other services (like Gitorious, or even non-git hosting),
it would be rendered useless.
3. The status really describes the code/project itself, not the GitHub repository per se, so it should live with the code.

So, I'm brainstorming a straightforward semi-standardized way of communicating this information. Assuming
it's not implemented in GitHub itself, but rather becomes part of the repository content, that poses some
interesting questions for both what information is communicated and how to communicate it. What follows is
really my brainstorming and initial ideas. I'd very much appreciate it if anyone who's interested submits
their ideas and comments. I fully intend to start using something like this for my own projects but, not to
be too arrogant, I think it's a useful idea and could benefit from some accepted standard.

What to Communicate
--------------------

The first question is what data to communicate. Ideally, this would be one of a standardized set of
repository/project status identifiers, along with a textual description that could be provided by
the author, for additional clarity. My humble suggestion (very much a WIP) of the possible statuses,
along with the suggested (canonical) description of their meanings:

* __Concept__ - Minimal or no implementation has been done yet.
* __WIP__ - Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.
* __Suspended__ - A WIP project that has had work stopped for the time being; the author(s) intend on resuming work.
* __Abandoned__ - A WIP project that has been abandoned; the author(s) do not intend on continuing development.
* __Active__ - The project has reached a stable, usable state and is being actively developed.
* __Inactive__ - The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.
* __Unsupported__ - The project has reached a stable, usable state but the author(s) have ceased all work on it. A new maintainer may be desired.

I assume that there might be some dissenting opinions on whether this list of statuses is complete, or perhaps too long.
However I feel that it's the minimum set required to describe a project along the two axes which I consider important:
usability (is the code here complete enough to "work" for something) and support/development status (is it being worked on,
or are there plans to do so in the future). I'm certainly open to opinions on this.

How to Communicate It
---------------------

I view this as a more complex question technically, as doing this within the repository content (instead of in a GitHub API)
necessarily involves polluting that repository. My main two technical requirements (at least with my own intended use in mind)
are that the status be readable both by human and machine, and that the status should be available in one place within the
repository (i.e. in only one place for both humans and machines, and not requiring any transformation).

The best I've been able to come up with so far is either including the status in a special file (likely a specially-named dotfile),
or including it in the README. The dotfile method is optimized for machine-reading - it would be a single file, likely named
".repostatus.org", with a simple specified format. It's easy and cheap for a machine to find and parse, and shouldn't be too cumbersome
to add. But it pollutes the repository with another file, and worse, it would be quite unlikely to be found by a human who isn't
familiar with this practice, so it loses a lot in terms of human readability and intuitiveness.

On the other hand, adding something special to the README file is much more human-centric. The "something" could be a simple
string or link, or even better, a [badge](http://shields.io/). It would appear clearly when rendered on GitHub, and should also appear anywhere
else the readme is rendered (i.e. in online documentation or in packages of the project). However, this poses a few challenges:

1. It wouldn't necessarily be possible to have a status that's machine-readable but not rendered to the human observer. Sure, this
sort of goes against half of the purpose of this idea, but some people probably wouldn't want this extra piece of information
cluttering up their README. It's possible to put comments in [rST](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#comments),
but [markdown support](http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax) isn't nearly as reliable,
being a bit of a hack.
2. This is optimized for human readers. In order to be detected by machine, the repository would need to be searched for
a readme file (even assuming the convention of "^README*", there's a myriad of possible file extensions that could be used),
which isn't necessarily a cheap operation (especially since it would require access to the file listing within the repository).
3. Furthermore, machine detection would need to be able to either parse the markup (if any), or do string search on the file
contents. Once again, a more expensive operation.

Current Theory
---------------

At the moment, I'm leaning towards this theory of implementation:

Badges are placed in the project's README indicating the status. The badges would be sourced from specified URLs, served
by [repostatus.org](http://repostatus.org) and linked to specified URLs describing the status (likely of the form
http://repostatus.org/1.0/#active). Machine determination of status would be made by a string match for one of
the specified status URLs - nothing more is needed. It would be simple enough to simply specify that, for machine
determination, the first file in the repository (sorted in lexicographical order) beginning with "readme" (case-insensitive) and containing
a matching URL determines the status. For human users, the badge image could be combined with descriptive alt-text, and
possibly followed by a more descriptive explanation, if the author chose so. This would eliminate the need for a fixed
set of possible readme file names, and the need for machine identification to be able to parse all possible markups.


The visual impact to the readme document (assuming it's rendered) would be minimal. Here are some quick takes on
a first set of badges, along with the alt text set on them (which could be changed by the user, or also included
in plain text next to the badge).

* ![Repo Status: Concept - Minimal or no implementation has been done yet.](http://img.shields.io/badge/repo%20status-Concept-ffffff.svg) Repo Status: Concept - Minimal or no implementation has been done yet.
* ![Repo Status: WIP - Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](http://img.shields.io/badge/repo%20status-WIP-yellow.svg) Repo Status: WIP - Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.
* ![Repo Status: Suspended - A WIP project that has had work stopped for the time being; the author(s) intend on resuming work.](http://img.shields.io/badge/repo%20status-Suspended-orange.svg) Repo Status: Suspended - A WIP project that has had work stopped for the time being; the author(s) intend on resuming work.
* ![Repo Status: Abandoned - A WIP project that has been abandoned; the author(s) do not intend on continuing development.](http://img.shields.io/badge/repo%20status-Abandoned-000000.svg) Repo Status: Abandoned - A WIP project that has been abandoned; the author(s) do not intend on continuing development.
* ![Repo Status: Active - The project has reached a stable, usable state and is being actively developed.](http://img.shields.io/badge/repo%20status-Active-brightgreen.svg) Repo Status: Active - The project has reached a stable, usable state and is being actively developed.
* ![Repo Status: Inactive - The project has reached a stable, usable state and is no longer being actively developed; support/maintenance will be done as time allows.](http://img.shields.io/badge/repo%20status-Inactive-yellowgreen.svg) Repo Status: Inactive - The project has reached a stable, usable state and is no longer being actively developed; support/maintenance will be done as time allows.
* ![Repo Status: Unsupported - The project has reached a stable, usable state but the author(s) have ceased all work on it. A new maintainer may be desired.](http://img.shields.io/badge/repo%20status-Unsupported-lightgrey.svg) Repo Status: Unsupported - The project has reached a stable, usable state but the author(s) have ceased all work on it. A new maintainer may be desired.

If the readme is (for some strange reason) primarily intended for a non-rendered view, it would be acceptable to
include just the URL to the status description, optionally with some human-readable text.

I'll probably start using something like this for my personal projects. I intend on even writing up a spec
for the README-based variant, along with some formatting and parsing/machine identification rules. Any and
all comments are welcome. This is the result of a few hours' sporadic thought one afternoon, so I'm sure there
are some major issues I haven't realized yet. Please pass them along, or tell me if this is of any interest to you.
