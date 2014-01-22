Title: Adding Piwik Web Analytics Integration to ViewVC
Date: 2012-03-23 21:15
Author: admin
Category: Tech HowTos
Tags: analytics, piwik, python, subversion, svn, tracking, viewvc
Slug: adding-piwik-web-analytics-integration-to-viewvc

All of my public [subversion repositories][] and [CVS repositories][]
are available online through a great Python application called
[ViewVC][], which provides a web-based interface to CVS and SVN
repositories, as well as history browsing, graphical diffs, etc. An
amazingly large amount of the traffic to my web server is for the vhosts
that serve this, so I decided that I should add some analytics to it.
I'm in the process of trying out [Piwik][], a full-featured,
GPL-licensed, self-hosted alternative to [Google Analytics][]. It gives
lots of useful information like number of visits and unique visits per
page, search engine keywords, referrers, average time on page, bounce
rate (number of one-page visits), etc.

I have ViewVC installed from the [RPMforge packages][], so there's one
code base for both of my vhosts. This means that I can't simply slap the
tracking code at the bottom of the templates and call it a day. I opted
to go for a nicer solution, and what follows is a patch (diff -u) to the
current (1.1.13) version of ViewVC that adds a "piwik" section to
viewvc.conf, and adds the piwik tracking code with the specified base
URL and site ID into all ViewVC pages. Enjoy.

~~~~{.diff}
diff -ru viewvc-ORIG/lib/config.py viewvc/lib/config.py
--- viewvc-ORIG/lib/config.py   2012-01-25 08:31:52.000000000 -0500
+++ viewvc/lib/config.py    2012-03-23 21:57:08.000000000 -0400
@@ -108,6 +108,7 @@
     'query',
     'templates',
     'utilities',
+    'piwik',
     )
   _force_multi_value = (
     # Configuration values with multiple, comma-separated values.
@@ -127,6 +128,7 @@
                'options',
                'templates',
                'utilities',
+               'piwik',
                ),
     'root'  : ('authz-*',
                'options',
@@ -461,7 +463,14 @@
     self.cvsdb.check_database_for_root = 0
 
     self.query.viewvc_base_url = None
-    
+
+    # begin  patch for piwik integration
+    self.piwik.use_piwik = 0
+    self.piwik.base_url = ''
+    self.piwik.site_id = ''
+    self.piwik.use_jsindex = 0
+    # end  patch for piwik integration
+   
 def _startswith(somestr, substr):
   return somestr[:len(substr)] == substr
 
diff -ru viewvc-ORIG/templates/include/footer.ezt viewvc/templates/include/footer.ezt
--- viewvc-ORIG/templates/include/footer.ezt    2012-01-25 08:31:52.000000000 -0500
+++ viewvc/templates/include/footer.ezt 2012-03-23 22:03:04.000000000 -0400
@@ -13,5 +13,17 @@
 
 
 
+[is cfg.piwik.use_piwik "1"]
+
+var pkBaseURL = (("https:" == document.location.protocol) ? "https://[cfg.piwik.base_url]/" : "http://[cfg.piwik.base_url]/");
+document.write(unescape("%3Cscript src='" + pkBaseURL + "[is cfg.piwik.use_jsindex "1"]js/[else]piwik.js[end]' type='text/javascript'%3E%3C/script%3E"));
+
+try {
+var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", [cfg.piwik.site_id]);
+piwikTracker.trackPageView();
+piwikTracker.enableLinkTracking();
+} catch( err ) {}
+
+[else][end]
 
 
Only in viewvc-ORIG/templates/include: header.ezt~
diff -ru viewvc-ORIG/viewvc.conf.dist viewvc/viewvc.conf.dist
--- viewvc-ORIG/viewvc.conf.dist    2012-01-25 08:31:52.000000000 -0500
+++ viewvc/viewvc.conf.dist 2012-03-23 21:44:02.000000000 -0400
@@ -1131,3 +1131,29 @@
 #viewvc_base_url =
 
 ##---------------------------------------------------------------------------
+[piwik]
+
+## This section enables Piwik  web analytics tracking.
+## If piwik is enabled (use_piwik = 1) all other options must be specified.
+##
+## This is based on a patch by Jason Antman  
+## to ViewVC 1.1.13, written 2012-03-23.
+## The latest version of the patch, and information on it, can always be found at:
+## 
+##
+##
+## To enable piwik, change use_piwik to 1. Set to 0 to disable
+use_piwik = 1
+##
+## Set base_url to the hostname and path to your piwik installation, with no trailing slash.
+## i.e. piwik.example.com or www.example.com/piwik
+base_url = piwik.example.com
+##
+## Set to the numeric id of your website in Piwik
+site_id = 5
+##
+## Set to 1 if you want to use js/index.php to serve the tracking code, 
+## or leave at 0 if you want to call piwik.js directly
+use_jsindex = 0
+
+##---------------------------------------------------------------------------
\ No newline at end of file
~~~~

  [subversion repositories]: http://viewvc.jasonantman.com
  [CVS repositories]: http://cvs.jasonantman.com
  [ViewVC]: http://viewvc.org/
  [Piwik]: http://piwik.org
  [Google Analytics]: http://www.google.com/analytics/
  [RPMforge packages]: http://pkgs.repoforge.org/viewvc/
