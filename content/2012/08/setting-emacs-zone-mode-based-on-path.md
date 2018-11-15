Title: Setting emacs zone-mode based on path
Date: 2012-08-15 08:00
Author: admin
Category: Software
Tags: bind, emacs, lisp, named, zone-mode
Slug: setting-emacs-zone-mode-based-on-path

At work, we do a fair amount of DNS updates. Our zone files are stored
in subversion, and are named according to the domain (with no .zone
extension). It's a real pain when updating a few (or a few dozen) zones
in Emacs, since I have to remember to "M-x zone-mode" so the serial gets
automatically updated. Here's a lisp snippet to put in your `.emacs`
file that will set zone-mode for all files in any path matching the
regex `svn/named/zones-internal`. I deliberately made it a relative path
(or, really, any path containing that) so it would work for all of my
team's workstations, no matter where we have the svn repo checked out:

~~~~{.common-lisp}
(add-to-list 'auto-mode-alist '("svn/named/zones-internal/" . zone-mode))
~~~~

Many thanks to `taylanub` on #emacs on irc.freenode.net for helping
with this.
