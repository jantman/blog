Title: Ignoring SVN directories and save files with grep
Date: 2010-10-15 07:27
Author: admin
Category: Tech HowTos
Tags: grep, linux
Slug: ignoring-svn-directories-and-save-files-with-grep

Yes, I know I haven't posted anything useful in a while. I've been quite
busy at work, and hopefully I'll post some of my DHCP stuff. In the
meantime...

I'm starting a project for the [ambulance
corps](http://www.midlandparkambulance.com/) migrating two Linux boxes
to a single new server. One of them has been in production for about
five years, and (partially due to the "we need it yesterday" nature of
emergency services) has quite a bit of cruft laying around. Since almost
everything is web-based (well, browser-based, restricted to the LAN
only), there are a lot of web apps and PHP scripts that need to be
migrated. This is made even more complicated by the switch from SuSE
10.1 (yes, ancient) to CentOS 5.4, and therefore from `/srv/www/htdocs`
to `/var/www/html`. I could be lazy and symlink it, but I think it's
time to search down and destroy any absolute includes.

The problem with doing this is that, with any scripts in SVN, grepping
for a string could potentially return three hits for a file - the actual
file, the emacs save file (`filename~`) and the text file in the `.svn`
directory.

The solution is actually pretty easy. To get rid of the .svn
directories, we add `--exclude=\*.svn\*` to our grep command line (yes,
I know, it excludes everything with ".svn" in the path, but that's
acceptably imprecise for my purposes). To get rid of the tilde (save)
files, all we need is `--exclude=\*~`. It's no problem to string them
together as `grep --exclude=\*~ --exclude=\*.svn\* -rin "foo bar" *`.

<p>
To make this even easier, just add to your `.bashrc`:

~~~~{.bash}
export GREP_OPTIONS="--exclude=\*~ --exclude=\*.svn\*"
~~~~

</p>

