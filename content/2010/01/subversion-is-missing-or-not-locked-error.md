Title: Subversion 'is missing or not locked' error
Date: 2010-01-29 15:58
Author: admin
Category: Miscellaneous
Tags: subversion, svn, version control
Slug: subversion-is-missing-or-not-locked-error

Recently I was doing some work on a few PHP scripts, and came by a
rather annoying error while trying to commit to subversion:

~~~~{.text}
svn: Commit failed (details follow):
svn: Working copy '/srv/www/htdocs/newcall/stats/generated' is missing or not locked
~~~~

The problem was a directory, "generated". This particular app makes use
of [libchart](http://naku.dohcrew.com/libchart) to draw simple charts in
PHP. Libchart writes the charts to files, and therefore needs a
directory writable by the Apache user. So, I created the `generated/`
directory for these output files, and `chown`ed `wwwrun:www`. Now,
apparently, the subversion `svn add` command doesn't check
ownership/writable permissions before adding a directory. So, it added
`generated/` to the main list of files, but couldn't write the `.svn`
directory and add a lock. IMHO, this is an error in the svn client.

I couldn't find any solutions to the problem online. Essentially, I have
an empty directory (or at least nothing useful in it) that got partially
added to svn - it was added to the `.svn/entries` file in the parent
directory, but never had its own `.svn` directory created.

The only solution that I found is to manually edit the `.svn/entries`
file in the parent directory. **WARNING:** this isn't for the faint of
heart. Be sure you don't screw anything up.

1.  Open the `.svn/entries` file in the parent directory in a text
    editor (i.e. if the problem directory is `stats/generated`, edit
    `stats/.svn/entries`
2.  Find the `entry` node with the correct "name" attribute for the
    directory in question. For stats/generated, in the
    `stats/.svn/entries` file, it should look like:

~~~~{.xml}
<entry
   name="generated"
   kind="dir"
   schedule="add"/>
~~~~

3.  Make the entries file writable (`chmod u+w entries`)
4.  Remove the entry from the file.
5.  Set the entries file back to non-writable (`chmod u-w entries`)
6.  Remove any save files if they were created (i.e. `entries~` for
    emacs)
7.  Remove the directory itself and re-create it, this time adding to
    svn before setting the ownership.
8.  Commit. It should now work.

