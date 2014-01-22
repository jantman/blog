Title: Access control in ViewVC
Date: 2007-07-25 12:00
Author: admin
Category: Tech HowTos
Tags: cvs, viewvc
Slug: access-control-in-viewvc

ViewVC (www.viewvc.org), a popular web-based frontend to CVS and SVN,
has no access control mechanism, nor does CVS. As a result, when using
ViewVC, anyone who can see the web page can browse, download, and view
files in the entire CVS repository. While I initially loved this, as I
used CVS only for GPL'd projects and snippets of useful code, after a
while I decided to put some admin scripts in CVS. Most of them aren't
really sensitive, but provide a bit more of a look at the workings of my
systems than I had hoped.

I tried unsuccessfully to implement Apache Auth on the URL. After
sitting around for a while, I hit upon a wonderfully simply (yes,
inelegent) solution.

Being that ViewVC runs as a CGI script, it runs as the user and group of
the webserver - in my case, user 'www' and group 'wwwrun'. How to
protect one directory in the repository from being viewed with viewvc?
Well, the CVS user 'cvsuser' runs as a member of group 'users'. My main
username, 'jantman', owns all of the files in the repo. As a result, the
permissions required for CVS to run currectly and for all local users to
use it, are simply to have the directories in the repository owned by
some user and the group 'users', while giving both user and group rx
permissions to the directory (and, obviously, the user at least should
have rwx).

To protect a given directory/module "foo" in your cvsroot from being
viewed under ViewVC:

<li>
Make sure the directory is owned by someuser and group 'users'.

<li>
`chmod -R o-rwx foo"` - no permissions at all for 'other'

As your web server (and, therefore, the CGI script viewvc.cgi) run as
user 'www' and group 'wwwrun', they cannot access the directory 'foo' at
all. When you attempt to view the file listing or any file in ViewVC,
you get a read error (incorrect permissions).

A kludge? Yes. Are there ways around it? Yes. But it gets the job done,
and allows me to continue using my existing infrastructure.
