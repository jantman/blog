Title: Bug/Issue Tracking - Update / Review of Eventum
Date: 2007-09-17 14:47
Author: admin
Category: Projects
Tags: bug tracking, eventum, PHP, review, ticketing
Slug: bugissue-tracking-update-review-of-eventum

So, after many hours of investigating potential bug/issue tracking
packages, I have chosen one. And gone live with it, all in one weekend.
After much evaluation, my final choice was
[Eventum](http://eventum.mysql.com/) from MySQL (I'm using the current
version, 2.0.1). I will admit that it is not perfect. There are some
features I wanted that weren't there, and the documentation is awful.
But it's written in PHP.

That being said, it is very much a community-driven project. The support
on the mailing list, both from other community members and from Bryan
Alsdorf, has been wonderful. I had some issues viewing the help
documents, specifically those in pop-ups, but I've been told that most
new documentation has been moved to the wiki at the link above.

The project provides for advanced bug- and issue-tracking including time
tracking, file attachments, and customizable statuses, priorities, and
categories. It also provides email integration, both in terms of sending
email alerts and opening issues (as well as updating and tracking) by
parsing incoming emails. The email alerts worked out-of-the-box, but I
did not configure parsing of emails.

One of my main requirements which was met perfectly by Eventum is its'
ability to easily handle multiple projects. It also has a built-in
capability to allow anonymous issue submission (enabled on a
project-by-project basis). You can define custom fields for issues on a
project-by-project basis, and set them as required fields for either
registered users, anonymous users, or both.

One feature that I found lacking was the possibility for a user to view
all of the open issues assigned to them. Currently, all user interface
is on a project-by-project basis. Therefore, listing of open issues is
only available for the currently selected project. To cope with this, I
hacked together a little PHP script that just queries the database for
issues by user and displays it in a simple little page.

One of the major features about Eventum that caught my eye was
integration with a version control system (SCM, as far as the Eventum
docs are concerned). The feature list stated integration with CVS and
SVN. When I actually looked into integrating it with CVS, however, the
problems began. Firstly, the javascript-based help popup would not
display anything, let alone the proper page. Installation was otherwise
perfect under Apache2. I was forced to browse to the included HTML file
manually and check it out. The overview seemed simple enough - throw a
script in your CVSROOT loginfo file, update a few variables in the
web-based Eventum configuration, and you're off to the races. Reading
on, I found that the installation page was a confusing jumble of
references to a deprecated perl script and the current PHP script to
call from loginfo. Furthermore, database access is provided by having
the script called from loginfo parse the logging information and then
*run a HTTP GET* on a local script served in the Eventum web
directory. This added level of abstraction not only confuses me to no
end, but also introduces the possibility for malicious users to insert
data in the Eventum SCM database simply by visiting a well-known URL.

More importantly, the script provided to be called by loginfo seems to
expect the old CVS logging format, not the new one being provided by my
installation of CVS 1.12.12. While annoying, this ended up being a minor
fix in the provided "process\_cvs\_commits.php" - I simply had to
rewrite the argument parsing code so that it no longer expects the file,
old version, and new version (%{sVv}) information to be space-separated
on the command line in the form of s,V,v tuples, but expects everything
to be space-separated. I should be cleaning up my fix a bit and
submitting it for inclusion in the next release.

Once patched, CVS integration works perfectly. Simply append an
identifier to the end of your commit log message, such as "(issue: 21)"
or "(bug: 21)" and the commit will be automatically associated with the
issue of that number. When viewing an issue, a list of associated CVS
commits can be viewed.

It must be remembered that, as I have read, Eventum is used internally
by MySQL. It is, therefor, a mature project that is well tested in one
circumstance. I believe that it is mature and generally well-working
(though I've heard reports that the 2.x tree isn't as stable as the
older versions, which are most likely still in use at MySQL). It must
also be noted that the issue with CVS integration is most likely only
with the newer CVS versions using the new logging format (I don't know
when the switch was made) and will probably not be noticed in older
projects which have established CVS systems.

Now, for the opinion section. Eventum has thousands of features. I have
detailed every issue that I have, which total about five. I found it to
be a stable system, ready-to-run out of the box. Overall, I think it has
the best feature set of the open-source bug tracking systems that I
surveyed, which are probably most of the ones out there. It's a great
project which I'd recommend to anyone, though if you want more advanced
features (like integration with CVS, or things not offered such as
anonymous issue viewing) you should be comfortable with coding in PHP
until someone makes patches available.
