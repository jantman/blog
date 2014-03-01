Title: Blog Moved from Self-hosted WordPress to Pelican on GitHub Pages
Date: 2014-03-01 14:14
Author: Jason Antman
Category: Miscellaneous
Tags: blog,wordpress,pelican,github
Slug: blog-moved-from-self-hosted-wordpress-to-pelican-on-github-pages
Summary: My blog is finally migrated from self-hosted WordPress to Pelican on GitHub Pages. Quite an ordeal.

I just finally finished my migration from self-hosted WordPress to [Pelican](http://getpelican.com), a Python-based
static site generator, hosted on [GitHub Pages](http://pages.github.com/). It's not only easier and free, but also the
first step in my plan to migrate off of my [Linode](http://linode.com) VM and onto a mix of EC2 and free services.

I'm sure this post will be [around in five years](/2009/02/wordpress-installation-finished/) when there's a smarter way
to do all this, but until then... yay!

I hit a number of bumps during the migration, mainly around [Migrating HTML posts from WordPress to Markdown in Pelican](/2014/02/converting-wordpress-posts-to-pelican-markdown/)
and migrating [WordPress comments to Disqus](/2014/03/wordpress-to-pelican-with-disqus-comments/), but in the end everything
seems to be working. Hopefully someone will find this and save a few hours or days of work if they try the same thing.

Post-go-live I still had some issues - Disqus was displaying an error:

> We were unable to load Disqus. If you are a moderator please see our troubleshooting guide.

on all posts created after the WordPress migration, and FeedBurner rejected my attempts to change the RSS feed URL to
its new value (though I'm pretty sure that's because I neglected to drop the TTL on the DNS record, and I can't
find a way to tell Feedburner to purge it from cache).
