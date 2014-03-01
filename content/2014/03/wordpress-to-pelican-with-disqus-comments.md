Title: Wordpress to Pelican with Disqus comments
Date: 2014-03-01 09:09
Author: Jason Antman
Category: Tech HowTos
Tags: wordpress, pelican, blog, disqus, comments
Slug: wordpress-to-pelican-with-disqus-comments
Summary: Solutions to some of the many problems converting a WordPress blog to a Pelican blog with Disqus for commenting.
Status: draft

This is the second part of my WordPress to [Pelican](http://getpelican.com) conversion saga.
In the [last post](/2014/03/converting-wordpress-posts-to-pelican-markdown/) I ran through some
of the issues that I faced when converting the posts themselves, setting up my theme and settings,
etc. In this post, I'll discuss the saga of moving from WordPress comments to Disqus comments.

Be sure to read **all** of this before trying it yourself, as I had some serious problems with my
first attempt.

## Initial Import to Disqus

Initially, I installed the Disqus WordPress plugin as instructed in
[Disqus' Import from WordPress documentation](http://help.disqus.com/customer/portal/articles/466255-importing-comments-from-wordpress).
The automatic import imported three of 134 comments, and froze there,
even though the status said it was 100% complete. I emailed Disqus' support,
and was told that this meant the import failed (even though there was no explicit
notification, their admin UI said the import was successful) and I had to manually
import my comments. I did this, as instructed in the same docs, by disabling all
plugins except for Disqus and generating an XML export from WordPress, then re-enabling
the plugins, and uploading the export to Disqus. This time, I ended up with all 134
comments in Disqus, so I assumed that all went well.

## Previewing Comments in Pelican

I added my Disqus ``shortname`` to the ``DISQUS_SITENAME`` field in ``pelicanconf.py`` and
re-built. I ended up having an issue with ``SITE_URL`` being set incorrectly for some testing
that I did, so that killed 10 minutes. I rebuilt locally with ``SITE_URL`` not defined, and
then used ``fab serve`` to serve locally. I was using my
[Planning Migration from Wordpress to Static Site](/2014/01/planning-migration-from-wordpress-to-static-site/)
post to test, as it was both the most recent post, and had a five comments in WordPress, which imported
correctly into Disqus and were visible both in the Disqus moderation tool and on the now-Disqus-powered
WordPress blog.

Once I rebuilt with ``DISQUS_SITENAME`` set and served locally with SimpleHTTPServer (``fab serve``),
I checked the post and saw only a "We were unable to load Disqus" message below the post. It contained
a [link to their help article for that problem](http://help.disqus.com/customer/portal/articles/472007-i-m-receiving-the-message-%22we-were-unable-to-load-disqus-%22),
which pointed me at a domain mismatch/different origin problem. As indicated on that page,
I went to Settings -> Advanced in the Disqus admin, found the "Trusted Domains" box, and added
both my test domain (newblog.jasonantman.com - pointing at GitHub pages until I was ready to
shut WordPress down and actually move the live site) and "localhost" for testing, and saved.

I refreshed the page I was looking at, and now could see the Disqus commenting below my post,
but it wasn't showing any of the comments yet.

![Disqus commenting with no comments](/GFX/disqus_wrong_url.png)

I pulled up the source of the page, and saw in the Disqus javascript just below the post content:

~~~~{.js}
            var disqus_shortname = 'jasonantman'; // required: replace example with your forum shortname
            var disqus_identifier = 'planning-migration-from-wordpress-to-static-site';
            var disqus_url = '../../../2014/01/planning-migration-from-wordpress-to-static-site/';
~~~~

Everything looked OK to me except for ``disqus_url``, which I'd seen mention of on the
[help page](http://help.disqus.com/customer/portal/articles/472007-i-m-receiving-the-message-%22we-were-unable-to-load-disqus-%22)
I'd just been looking at. Sure enough, it indicated that the ``disqus_url`` var must be
an absolute URL to the post, not a relative path. I assume this was because I'd generated
the content without having ``SITE_URL`` set, so I hand-edited the generated page to change this
to the correct URL, http://blog.jasonantman.com/2014/01/planning-migration-from-wordpress-to-static-site/,
and tested again. Unfortunately, still zero comments.

## WordPress Disqus Plugin Permalinks

Fearing the worst, I pulled up the same post on my now-Disqus-powered WordPress blog,
and took a peek at the source. The javascript over there revealed a problem:

~~~~{.js}
    var disqus_url = 'http://blog.jasonantman.com/2014/01/planning-migration-from-wordpress-to-static-site/';
	var disqus_identifier = '1546 http://blog.jasonantman.com/?p=1546';
	var disqus_container_id = 'disqus_thread';
	var disqus_domain = 'disqus.com';
	var disqus_shortname = 'jasonantman';
	var disqus_title = "Planning Migration from WordPress to Static Site";
~~~~

While the URL is correct, the Disqus WordPress plugin uses the WordPress
post ID and permalink for the "identifier", but the Pelican plugin uses the slug.
That's a problem, as my Pelican site will have the same URLs, but the WordPress
post-ID-based permalinks are gone (since it's a static site, and there's no easy
way of replicating things that are query param based). The WordPress post IDs
are thrown out by Pelican, so there's no way to connect the two.

Even worse, I remembered that Disqus'
[Importing Comments from WordPress help page](http://help.disqus.com/customer/portal/articles/466255-importing-comments-from-wordpress)
clearly stated:

> Imported comments can't be permanently deleted. Consider following our [guidelines for development sites](http://help.disqus.com/customer/portal/articles/1053796-best-practices-for-staging-development-and-preview-sites) to make sure the data you're importing is correct. You can [register a new forum](http://disqus.com/register) if you have imported the wrong comments.

## Solution to Permalink Issue

Not seeing any way around it, I figured it was time to "bite the bullet". I disabled the Disqus plugin
in WordPress and then installed and activated the
[WordPress Code Freeze Plugin](http://wordpress.org/extend/plugins/code-freeze/)
to disable comments. (*Note* ironically, this plugin also uses JavaScript to disable your ability to
deactivate plugins, including itself. So before you activate it, copy the "Activate" link and save it
somewhere; changing ``action=activate`` to ``action=deactivate`` will let you get rid of it if you want).

Disqus has some documentation on [Importing and Exporting](http://help.disqus.com/customer/portal/articles/1104797-importing-exporting)
which includes [Custom XML Imports](http://help.disqus.com/customer/portal/articles/472150) based on the
WordPress XML export format. So, I figured that I just had to decide that WordPress commenting would be
turned off, and do a point-in-time migration to Disqus (maybe circling back to hack the Disqus WP plugin
to keep comments working there for the time being).

Before anything else, I decided to actually set up a test forum/site in Disqus like they suggested.
I updated the ``DISQUS_SITENAME`` in ``pelicanconf.py``, and then started in on the XML munging. The
[Custom XML Imports](http://help.disqus.com/customer/portal/articles/472150) documentation implies
that the import engine recognizes a ``dsq:thread_identifier`` XML element that holds the thread identifier,
but that element wasn't present in my WordPress XML export. It appeared that Disqus was concatenating the
``wp:post_id`` and ``guid`` fields (with a space in between) to come up with the identifier.

So, I wrote a script ([wp_comment_xml_munge.py](https://github.com/jantman/blog/blob/master/dev/wp-move/wp_comment_xml_munge.py))
using [lxml](http://lxml.de/) that adds the ``dsq:`` namespace to the WordPress XML export (unfortunately using
string replacement and a temp file, due to a [bug in lxml](https://bugs.launchpad.net/lxml/+bug/555602))
and then adds the ``dsq:thread_identifier`` tag to each post item, setting its value to the same
string as ``wp:post_name``, the URL slug (and post identifier in Pelican).

I imported the XML written by the script into my test forum in Disqus and rebuilt the Pelican content.
Magically, the first time I looked, the comments were there.

Now, time to see if I could get the same effect with the existing Disqus site/forum:

1. In the Disqus moderation interface, delete all comments. You'll have to do this in batches of 10, as that's
   how they're paged in the interface. The comments don't seem to be permanently deleted, but do show as "deleted".
2. Go to [import.disqus.com](http://import.disqus.com) and select your "forum" (site). You should see your existing
   (previous) import, as 100% complete, with the correct count of threads and comments. Do another import with the
   ``_disqus.xml`` munged XML export.
3. Comments should now be linked to the correct post in Pelican.

At this point, Pelican seemed to be working, but WordPress was still left with only the old internal commenting,
and that was disabled by the Code Freeze plugin. I probably could have manually patched the Disqus plugin to
reflect the new thread identifiers, but instead, I chose to just push forward with the switch from WordPress to
Pelican.
