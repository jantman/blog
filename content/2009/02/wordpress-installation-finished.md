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
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /blog/
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule .* index.php [L]
</IfModule>
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
<?php
// redirect old Blogger URLs in /blog to new WordPress in /wp
$request = mysql_real_escape_string(str_replace("/blog", "", $_SERVER['REQUEST_URI']));

// handle constant stuff like feeds and top-level pages
// TODO
if(strpos($request, "_archive.html"))
{
    // redirect to an archive
    $request = substr($request, strpos($request, "/", 1)+1);
    $ary = explode("_", $request);
    $redirect_to = "http://blog.jasonantman.com/".$ary[0]."/".$ary[1]."/";
    header("Location: ".$redirect_to);
    die();
}
elseif(strpos($request, "labels/"))
{
    // redirect to a tag page
    $redirect_to = substr($request, strpos($request, "labels/")+7);
    $redirect_to = str_replace(".html", "", $redirect_to);
    $redirect_to = urldecode($redirect_to);
    $redirect_to = str_replace(" ", "-", $redirect_to);
    $redirect_to = "http://blog.jasonantman.com/tags/".strtolower($redirect_to)."/";
    header("Location: ".$redirect_to);
    die();
}
elseif(strpos($request, "/blogger.html"))
{
    // redirect to main blog
    header("Location: http://blog.jasonantman.com/");
    die();
}
elseif(strpos($request, "/atom.xml"))
{
    // redirect to new feed
    header("Location: http://blog.jasonantman.com/feed/");
    die();
}

// handle the posts, months, tags, etc.
$fail = false;
$redirect_to = "";
$conn = mysql_connect()   or die("Error. MySQL connection failed at mysql_connect");
if(! $conn)
{
    error_log("SCRIPT ".$_SERVER['PHP_SELF'].": "."Unable to connect to MySQL.");
    $fail = true;
}
$select = mysql_select_db('wordpress');
if(! $select)
{
    error_log("SCRIPT ".$_SERVER['PHP_SELF'].": "."Unable to select DB wordpress.");
    $fail = true;
}
$query = "SELECT m.meta_key,m.meta_value,p.post_name,p.post_date FROM wp_postmeta AS m LEFT JOIN wp_posts AS p ON m.post_id=p.ID WHERE m.meta_key='blogger_permalink' AND m.meta_value='".$request."';";
$result = mysql_query($query);
if(! $result)
{
    error_log("SCRIPT ".$_SERVER['PHP_SELF'].": "."Error in query: ".$query." ERROR: ".mysql_error());
    $fail = true;
}
if(mysql_num_rows($result) < 1)
{
    // couldn't find an appropriate page
    // TODO: find a better way... for now just redirect to the month page
    $ary = explode("/", $request);
    if(count($ary) > 3)
    {
        $redirect_to = "http://blog.jasonantman.com/".$ary[1]."/".$ary[2]."/";
    }
    else
    {
        $redirect_to = "http://blog.jasonantman.com/";
    }
}
else
{
    $row = mysql_fetch_assoc($result);
    $redirect_to = "http://blog.jasonantman.com/".date("Y", strtotime($row['post_date']))."/".date("m", strtotime($row['post_date']))."/".$row['post_name'];
}

if($fail)
{
    // redirect to main page with 302
    Header( "Location: http://blog.jasonantman.com/" ); // implicit 302
}
else
{
    // redirect to the post or month
    Header( "HTTP/1.1 301 Moved Permanently" );
    Header( "Location: ".$redirect_to );
}

?>
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
