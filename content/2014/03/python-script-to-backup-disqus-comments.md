Title: Python script to backup Disqus comments
Date: 2014-03-01 19:01
Author: Jason Antman
Category: Tech HowTos
Tags: pelican,disqus,python
Slug: python-script-to-backup-disqus-comments
Summary: Quick Python script to backup Disqus comments for a forum

Since I just [switched this blog to using Disqus for commenting](/2014/03/wordpress-to-pelican-with-disqus-comments),
I wanted a way to back up comments in case something goes wrong (like,
Disqus going the way of del.icio.us bookmarking).

I whipped up a quick [Python script](https://github.com/jantman/misc-scripts/blob/master/disqus_backup.py)
using the official [Disqus Python API client](https://github.com/disqus/disqus-python). It grabs the forum details,
threads list and posts (comments) list, and writes them out to a JSON file.

It doesn't have any restore feature, but it captures all of the data.

My first test made it look like there *may* be some posts and theads missing (my import from
wordpress showed 56 threads and 146 comments, but this script only grabbed 52 and 125 respectively),
so exercise some caution until I verify what the problem is. If you happen to figure it out,
please submit a PR.

The script is available on GitHub at [https://github.com/jantman/misc-scripts/blob/master/disqus_backup.py](https://github.com/jantman/misc-scripts/blob/master/disqus_backup.py).
