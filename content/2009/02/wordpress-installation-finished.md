Title: Wordpress Installation, Finished
Date: 2009-02-03 10:13
Author: admin
Category: Projects
Tags: apache, blogger, dynamic IP, wordpress
Slug: wordpress-installation-finished

Found this from a month and a half ago, waiting as a draft:

So, I mostly finished the WordPress installation. I got everything for
WordPress up and running, tested my Blogger URL redirection script and
then switched over my subdomain redirection.

The blogger redirection takes two parts, but is in fact quite simple.
First, I went into the directory where the Blogger content had lived -
`/srv/www/htdocs/blog` and moved everything in there into another
directory, out of the way. I then created a .htaccess in the directory
like:

~~~~{.apacheconf}

RewriteEngine On
RewriteBase /blog/
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule .* index.php [L]
~~~~

All this does is used mod\_rewrite to serve blog/index.php up for every
page request. In index.php, I handle the important URL forms for Blogger
- archives, tags, feeds, and posts - and redirect to the appropriate
place. For archives, I just parse out the year and month from the
Blogger URL and redirect to the proper page for WP. The feed is straight
redirection. The tags ("labels" in Blogger parlance) are pulled out of
the URL, have spaces (after `urldecode()`) replaced with dashes and are
redirected to the right tag for WP.

The posts, on the other hand, were a bit more difficult. My solution
ended up being parsing the post name out of the URL. When I used the
import tool, WP kept the original Blogger URLs in the `wp_postmeta`
table with a `meta_key` of "blogger\_permalink". I just looked for a
Blogger permalink matching the title from the Blogger URL, found the
corresponding post ID and redirected to the proper new WP URL.

The code for index.php, for me, looks something like:

~~~~{.php}
~~~~

</p>
So, it now looks like I'm pretty much done with setup, and even get to
keep my links. The one interesting problem that will crop up is due to
the fact that, at the moment, I'm hosting off of a dynamically IPed
residential internet connection, so I'm at
`http://jantman.dyndns.org:10011`. The problem lies in the fact that
Blogger used this for its' URIs and Permalinks, and it seems that
(though `http://blog.jasonantman.com` uses a 302 not a 301 to redirect)
Google, Technorati, etc. have indexed my site with this hostname and
port, instead of the redirecting subdomain. Normally this wouldn't be a
problem, but I plan on soon moving to a business hosting account with 5
static IPs and port 80 open. Which means that soon the subdomain will
become "real"... and all of those pesky dyndns.org:10011 links will be
obsolete. The only way I can think of fixing this is, once I make the
switch to static IP and port 80 (which will also include moving all of
my subdomains to name-based virtual hosts) I'll have to craft
RewriteRules or redirect rules to replace
`http://jantman.dyndns.org:10011/wp/` with
`http://blog.jasonantman.com/`, update DynDNS with my new static IP, and
keep a default vhost listening on 10011 to provide rule-based
redirection to the new subdomain. Eek.
