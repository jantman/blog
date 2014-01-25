Title: Meld - Graphical Diff Tool for SVN Directories
Date: 2012-03-12 09:48
Author: admin
Category: Tech HowTos
Tags: diff, kde, kdiff, meld, merge, subversion, svn
Slug: meld-graphical-diff-tool-for-svn-directories

I've been in the process of manually merging two directories in a
subversion repo. The second started out as a "development" copy of the
first (without branching, unfortunately). Since there's quite a few
files, I decided that a graphical diff program is a must. I usually use
[kdiff3](http://kdiff3.sourceforge.net), but my requirements for this
are a bit more stringent than usual: it has to handle recursive diffs on
two directories, and it has to be able to ignore SVN keywords (or an
arbitrary regex) since all of the files have keyword substitution on
LastChangedRevision and HeadURL. Kdiff3 supports [preprocessor
commands](http://kdiff3.sourceforge.net/doc/preprocessors.html) which
can include filtering the text through sed before performing the diff
(so I modified their regex to ignore version control keywords), but for
some reason (perhaps either bimary differences, or metadata differences)
I couldn't get the file difference indicator in the diretory tree view
to reflect this; even when ignoring keyword lines and whitespace, it
still showed every pair of files as different.

Enter [Meld](http://meldmerge.org/), a graphical diff project. I've only
used it for half an hour or so, but it seems wonderful. It's easy to
use, has a pleasing interface similar to
[Kompare](http://www.caffeinated.me.uk/kompare/), and even has simple
check boxes in the options menu to ignore whitespace and SVN keywords -
and they work! So far, I'm about half way through my 300+ file tree, and
the merge is going wonderfully.
