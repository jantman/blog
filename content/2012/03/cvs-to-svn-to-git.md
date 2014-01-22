Title: CVS to SVN to Git
Date: 2012-03-25 12:11
Author: admin
Category: Projects
Tags: cvs, git, svn, version control
Slug: cvs-to-svn-to-git

Thanks to some new interest, I've decided to resurrect an old project of
mine, [PHP EMS Tools][]. It's a web-based tool for small emergency
services organizations, mainly aimed at volunteer EMS/ambulance
providers. The tool handles roster tracking, scheduling, equipment
maintenance and checks, and a bunch of other administrative tasks. I
first started it in 2007 for the [Midland Park Ambulance Corps][]
(MPAC), which I was a volunteer EMT with from 2005 through 2011. I'll
admit that it's a perfect model of how not to run a software project.
The first few releases are plain awful code. I was keeping the project
in CVS at the time, and posted some early releases on [sourceforge][]
and FreshMeat, now [FreeCode][]. Sometime in 2009, I migrated the
contents of the trunk of the CVS module to a [SVN repository][], but
discarded the history. I also setup a MediaWiki-based website for the
project, giving some information and mainly asking for feedback. Around
that time I started working on a new and heavily updated (fixed) version
for MPAC, but since it appeared that there was no interest in the
project, and there were many many local customizations and
organization-specific features, I let their codebase diverge from what
was released, and as a result, stopped keeping it in version control.
Until now, when they need to migrate to a new server, and I've also
gotten some outside interest in the project.

So, as of this morning, I was left with at least four code bases:

1.  the original [CVS repository][] with branches and tags and some
    history, untouched since 2007
2.  the [SVN repository][] circa 2009, with only 3 commits, all related
    to the migration from CVS to SVN
3.  a "release" tarball that at least one outside organization is
    actually using.
4.  the code that MPAC is running, which has been largely rewritten
    since 2009, but also contains a lot of organization-specific
    customizations.

As a first step, I created a new SVN repository and migrated the
original CVS repo, complete with history, branches, and tags, to it
using [cvs2svn][], and then removed write permissions on the actual
module in the repository. This gave me a SVN repository with all of the
history of previous so-called releases, with a trunk matching r1 of the
"current" SVN repository. I then manually applied patches to trunk/ for
the two commits in the current SVN repository, and set the svn:date
revision property to the correct 2009 date for those commits. I also
confirmed that the correct tag matches up to the "release" tarball
mentioned above. So, I'm down to a "current" trunk, plus the locally
modified code running on MPAC's current server. My plan of action from
this point is as follows:

1.  Move the PHP EMS Tools website from Mediawiki to my local redmine
    installation, and update the news with a link to this post.
2.  Migrate the SVN repository, which now contains full history, to Git
    hosted at Github. Add Github integration to Redmine.
3.  Update freshmeat, sourceforge, and anywhere else online that knows
    about the project.
4.  Working in a git branch, begin converging the code MPAC is currently
    running with the latest (now git) trunk, trying to provide
    configuration options for anything organization specific, and
    testing as I go.

If all works well, I'll end up with MPAC running the current trunk, just
some different configuration options, and a working, up-to-date release.
The biggest issues are going to be how I handle the MPAC-specific
additions and customizations (a lot of stuff hard-coded for our position
titles, plus our very custom call report and telephone-based call-in
software, which is pretty tightly linked with the PHP EMS Tools core),
and how I balance abstracting things to be configurable for other users
versus getting this all done in a reasonable amount of time.

Stay tuned...

  [PHP EMS Tools]: http://www.php-ems-tools.com
  [Midland Park Ambulance Corps]: http://www.midlandparkambulance.com
  [sourceforge]: http://sourceforge.net/projects/php-ems-tools/
  [FreeCode]: http://freecode.com/projects/php-ems-tools
  [SVN repository]: http://svn.jasonantman.com/php-ems-tools/
  [CVS repository]: http://cvs.jasonantman.com/cgi-bin/viewvc.cgi/cvs/php-ems-tools-trunk/
  [cvs2svn]: http://cvs2svn.tigris.org/
