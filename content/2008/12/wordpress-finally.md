Title: WordPress... Finally!
Date: 2008-12-17 15:58
Author: admin
Category: Software
Tags: blogger, blogging, PHP, wordpress
Slug: wordpress-finally

Well, I finally bit the bullet. I woke up this morning, got in to work
(slow day) and said to myself, "My blog's finally moving to WordPress.
Today." So, I read through the docs (really psyched about the Blogger
import feature), downloaded 2.7 (latest), setup the DB and installed
away. Once I did the preliminary things like changing the admin password
and setting up some categories, I set about importing from Blogger.

Here was the first of the major issues. Though WordPress has really
hyped their Blogger importer, they failed to mention that it is totally
useless if you are self-hosting Blogger and publishing via FTP or SFTP,
as I was. So, after a lengthy consultation with the great oracle of
Google, I dedided I had two options - switch Blogger to publish to
BlogSpot.com and use the WP import tool, or custom hack a script. I must
admit, it felt a bit pointless... all of my old posts were in a directry
at the same level as WP, it seemed quite stupid to have to jump through
hoops to get that data. Though I'm not quite sure whether the GData API
really doesn't give access to posts if self-hosted.

I migrated publishing of Blogger to BlogSpot.com
([foobarthudgrunt](http://www.jasonantman.com/jargon/entry.php?id=metasyntactic-variable).blogspot.com),
despite worries about confusing Google or messing up the little bit of
ranking I've been able to gain. It successfully imported all 128 of my
entries, and the few comments. But, as I navigated to the "Edit" page to
have a look, an even bigger problem was apparent. All of the tags from
Blogger had ended up as categories in WP. So I had no tags for any of my
posts, and a gazillion categories with only one post in them. Luckily,
the DB schema is pretty sane, and I qickly figured out that both
categories and tags are stored in the `wp_term_taxonomy` table, and the
difference between a category and a tag is simply that the `taxonomy`
field is either "category" or "post\_tag", respectively. So, since I
hadn't added any posts in WP yet, I just changed `taxonomy` to
"post\_tag" for anything with an ID past the categories I'd added. And
it seems to have worked beautifully.

Up next, however, was the hard part: sitting down with my list of
categories and sifting through 128 posts to categorize them. The biggest
pain is the default edit posts table in the admin interface lists 15
posts per page, and with a cursory glance at the source I couldn't for
the life of me figure out where that limit is set.

Next up, I spent some time looking over the configuration options in WP,
updating my About page, and listing things to do in the future (more
static pages, blogroll and links, etc.).

I was finally ready to setup pretty URLs. And... sure enough... I
clicked "submit" to apply some changes to the default blog URL (my real
domain, as opposed to the DynDNS domain) and subtitle, and I got kicked
out of the admin interface. Try as I might, I had no luck logging in. I
then found that WordPress doesn't log anything anywhere - no MySQL log
and no error messages in the Apache error log. Wondeful. I spent about
an hour looking through the source, figuring out how the auth method
works, and trying to set an MD5 password. It was obviously apparent that
the password in the DB for my one user (administrative user) was
generated by PHPass, not MD5, but the auth function was evaluating
anything \>= 32 characters as PHPass, and the MD5 of my password was 32
characters, so that wouldn't work. I tried the "forgot password" link
with both username and email, but no mail was being sent. When I reached
the 2-1/2 hour mark, I started instrumenting the login code with some
`error_log()` lines to see what was up. I narrowed the problem down to
the block of code starting at lin 48 in `wp-include/user.php` -
specifically, according to the comments, no credentials were being
passed but the cookie wasn't set. And it's silent in that case. So, at
this point, I'm totally lost. I decided to clear all of my browser's
cookies and auth info, and try again. No dice. After nearly 3 hours, I
decided to do a packet capture, and found the horribly simple reason.
Somewhere in the code, WP is evaluating the "siteurl" or "home" values
from wp\_options, and using them instead of just doing relative links.
As a result, when the form submits, Apache keeps returning a 302, and
the form submission never makes it there. Hopefully this won't create a
problem when I transition from DynDNS to a real static IP and domain
name.

Next I enabled pretty permalinks, enabled mod\_rewrite in the vhost, and
selected a new template for my blog (though I'm planning on doing some
heavy customization). I didn't want to leave the default template up for
too long, in case Google's heavy crawling of my site picked up all of
the new content somehow... I ended up narrowing it down to three themes,
coincidentally all designed by
[mg12](http://wordpress.org/extend/themes/profile/mg12):
[Blocks2](http://wordpress.org/extend/themes/blocks2),
[iNove](http://wordpress.org/extend/themes/inove#post-668) or
[ElegantBox](http://wordpress.org/extend/themes/elegant-box). I
installed them all on my box and looked at iNove first, and it was love
at first sight.

So, that's where it stands right now. I finally have my blog on
WordPress and running, and have a theme. The action plan for tonight
includes:

-   Using RewriteRule and a PHP script to point all of the old Blogger
    URLs to the new WordPress installation.
-   Adding some new static content, and top-bar links to my other sites.
-   Refining the theme a bit, possibly?
-   Adding links to my sites, and to the blogroll.
-   Adding the buttons/plugins for del.icio.us, Digg, Slashdot, reddit,
    etc.
-   Redirecting my main blog page to WordPress.
-   Redirecting or linking my old feed locations to WordPress.

