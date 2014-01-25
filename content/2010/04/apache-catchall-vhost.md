Title: Apache catchall vhost
Date: 2010-04-07 10:10
Author: admin
Category: Tech HowTos
Tags: apache, catchall, PHP, web
Slug: apache-catchall-vhost

'; echo '

The page you are looking for is best found at:

'; echo '

**['.$newURL.']('.$newURL.')**

'; echo '

You will be automatically redirected after 5 seconds. If this does not
happen, click the link above.

'; echo '

'; }

</pre>
This script takes two distinct actions:

-   If the requested URL is `/` or `/index.php`, it transparently
    redirects to a different URL (and port).
-   Otherwise, it displays a "page moved to" message and uses a
    Meta-Refresh to redirect after 5 seconds.

