Title: Planning Migration from WordPress to Static Site
Date: 2014-01-01 15:15
Author: admin
Category: Miscellaneous
Tags: blog, jekyll, pelican, python, static site, wordpress
Slug: planning-migration-from-wordpress-to-static-site

Right now, this blog, my email, and a whole bunch of other services are
hosted on a [Linode][] Xen VM. I don't really keep up to date with
administration and upgrades the way I used to, and honestly, I'd rather
spend my time working on other things (like actually writing all of the
blog posts that I've been planning to. The first thing I've identified
for migration is this blog itself. It's currently on WordPress and,
frankly, I don't either need nor like it. But there are some features I
like. I'd like to end up with a static site generator, hosted from
either S3 or GitHub Pages. I know that means I'll lost comments (unless
I move to a third-party, JS-based comment system like [Disqus][], which
means I'll lose *control* over my comments) but I suppose I can live
with that. What I really want is something simple, static, cheap or free
(that I'll likely put behind a small ec2 instance running nginx for
redirects/rewrites).

I'm still in the planning phase, and trying to come up with a
feature-by-feature comparison of my options. I'll likely post that when
I finally have it done (at the moment it's in a very rough [Google Docs
spreadsheet][]). I'm trying to round up my static site generator options
and see which ones will do most, if not all, of what I want (though I
still haven't discounted using hosted wordpress if it comes down to it).
Here are the features I currently "use" (have) on my WordPress blog:

-   User-defined permalinks to posts
-   Overall RSS feed of blog (currently powered by FeedBurner) and of
    comments)
-   Categories (a post can be in multiple categories)
-   Tags
-   Category and Tag pages
-   per-Category and per-Tag feeds (RSS)
-   Tag cloud "widget" in sidebar
-   Themes. I actually like my current WP theme...
-   Visitor statistics (currently self-hosted [Piwik][], formerly Google
    Analytics)
-   Post publishing via cron'ed script (*see below*)
-   Draft/Pending status (i.e. let me save a partial post, and let me
    save a complete post but mark it "pending" so I can just publish it
    later)
-   Commenting (this will probably be the big sticking point)
-   Syntax hilighting
-   As "weird" as this is, I write all my posts in raw HTML, and am
    perfectly happy doing that.
-   "Subscribe via Email" FeedBurner widget
-   XML Sitemap
-   Twitter box/widget
-   Pingbacks (not that these are really useful for anything other than
    spam these days)
-   Automatic or manual post excerpts for feeds, etc.
-   Remote publishing via XML-RPC/Android app (not that I've used it
    more than once or twice)
-   Advertising - I currently use Google AdSense on my blog. The revenue
    from my tiny hit count isn't enough to offset the cost of a Linode,
    but if I moved to a much less expensive hosting service, it might be
    worth considering (you can't run ads on the free hosted WordPress,
    and I doubt you can on GitHub Pages either).

I should be updating this post when I do some more research and have a
comparison of the options.

Note on "Post publishing via cron'ed script" - sometimes I sit down and
write half a dozen or so blog posts at a time. But I don't want them all
to show up immediately, and spam the few people who still use RSS
readers after the death of Google Reader. So I set the posts to
"Pending" status, and I have a cron'ed script that runs every weekday
morning and publishes the one oldest "pending" post. Who knows if this
actually does any good or not...

  [Linode]: http://linode.com
  [Disqus]: http://disqus.com/
  [Google Docs spreadsheet]: https://docs.google.com/spreadsheet/ccc?key=0AnHh-ye5DNiNdF9DWkJrT2kzSkNsNVp6cjMzLXJ6VEE&usp=sharing
  [Piwik]: http://piwik.org/
