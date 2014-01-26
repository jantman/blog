Title: Apache catchall vhost
Date: 2010-04-07 10:10
Author: admin
Category: Tech HowTos
Tags: apache, catchall, PHP, web
Slug: apache-catchall-vhost

As mentioned in [one of my recent posts](/2010/04/bind9-dynamic-dns/), I occasionally
have to setup catchall pages in Apache. The general idea is usually that I either want
a vhost that serves one page for any conceivable request, or that I moved something and
want to alert the visitor, but provide a formula-based link to the new content. Assuming
you have `mod_rewrite`, this is relatively simple.

In your vhost configuration (or .htaccess), you just need two lines:

~~~~{.apacheconf}
RewriteEngine on
RewriteCond %{REQUEST_URI} !/index\.php$1
RewriteRule ^(.*)$ /index.php$1 [L]
~~~~

This will redirect every request for the vhost to <code>/index.php</code>. Within
your PHP script, you can access the actual request URI through `$_SERVER["REQUEST_URI"]`.
The script that I'm currently using for an internal page is:

~~~~{.php}
$newServer = "http://foo.example.com:12345";

if($_SERVER["REQUEST_URI"] == "/" || $_SERVER["REQUEST_URI"] == "/index.php")
  {
    header("Location: ".$newServer);
  }
else
  {
    $newURL = $newServer.$_SERVER["REQUEST_URI"];
    echo '<html><head><title>Page Moved</title>';
    echo '<META HTTP-EQUIV="refresh" CONTENT="5;URL='.$newURL.'">';
    echo '</head><body>';
    echo '<p>The page you are looking for is best found at:</p>';
    echo '<p><strong><a href="'.$newURL.'">'.$newURL.'</a></strong></p>';
    echo '<p>You will be automatically redirected after 5 seconds. If this does not happen, click the link above.</p>';
    echo '</body></html>';
  }
~~~~

This script takes two distinct actions:

1. If the requested path is `/` or `/index.php`, it transparently redirects to a different URL (and port).
2. Otherwise, it displays a "page moved to" message and uses a Meta-Refresh to redirect after 5 seconds.
