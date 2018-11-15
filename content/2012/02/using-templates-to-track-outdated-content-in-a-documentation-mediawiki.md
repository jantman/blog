Title: Using Templates to Track Outdated Content in a Documentation MediaWiki
Date: 2012-02-02 11:02
Author: admin
Category: Software
Tags: documentation, mediawiki, sysadmin
Slug: using-templates-to-track-outdated-content-in-a-documentation-mediawiki

Both my last and current jobs use [MediaWiki](http://www.mediawiki.org/)
for internal documentation. As always happens, some of this
documentation will inevitably get out-of-date, or totally deprecated. As
is also the case, many times when we're looking for docs in the middle
of an incident, we don't have the time to go back and fix what's wrong.
So, I devised the following template/category system to help keep track
of these problem pages.

First, create some templates that you will apply to the problem pages. I
use three - one for totally deprecated pages, one for pages that need
updating, and one for pages that just need cleanup. For the cleanup
template, in the MediaWiki search box, enter "Template:Cleanup" and
click "go". You should be told that the page doesn't exist, and given a
link to create the page. Create it, and enter the following content:

~~~~{.text}
[[Image:Cleanup.png]]

'''This page needs to be cleaned up or reorganized.'''

[[Category:Pages Needing Cleanup]]
~~~~

Now we create a category page for it, "Category:Pages Needing Cleanup",
with the content:

~~~~{.text}
__HIDDENCAT__

This category is for pages that are mostly correct and just need minor corrections or reorganization.

'''To add pages to this category''', include the following at the '''TOP''' of the page:

{{cleanup}}
~~~~

and save the page.

Now there's a few other changes we need to make. First, upload the
Cleanup.png graphic, which I got from wikimedia.org
[here](http://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Edit-clear.svg/40px-Edit-clear.svg.png)
and uploaded as Cleanup.png.

If you refresh the Template:Cleanup page, you should now see the image.
On a side note, "\_\_HIDDENCAT\_\_" on the category page prevents that
category from showing up in the category list at the bottom of the pages
we add to it, but this only works in MediaWiki 1.13 and up.

The last step is to add the [MediaWiki mbox
template](http://www.mediawiki.org/wiki/Template:Mbox) and its
dependencies. While I did this once before, I didn't really remember the
steps, but I found a post on [Glynor's
blog](http://glynor.com/2010/05/the-trouble-with-ambox-and-mbox/) that
details them rather nicely:

1.  Enable the [ParserFunctions
    extension](http://www.mediawiki.org/wiki/Extension:ParserFunctions).
    There are download and install instructions on the extension page,
    but you'll want to enable string functions. To do this, include the
    extension in LocalSettings.php like:

        :::php
        require_once( "$IP/extensions/ParserFunctions/ParserFunctions.php" );
        $wgPFEnableStringFunctions = true;

2.  Create a new page in your wiki called "Mediawiki:Common.css", and
    paste in the content from [MediaWiki.org
    MediaWiki:Common.css](http://www.mediawiki.org/wiki/MediaWiki:Common.css).
3.  Go to [Wikipedia's
    Special:Export](http://en.wikipedia.org/w/index.php?title=Special:Export)
    page, and enter "Template:Ambox" in the box, check off "Include
    templates", and export the template (and all dependencies) to a
    local XML file.
4.  Go to the "Special:Import" page of your wiki, and upload the XML
    file you just grabbed from Wikipedia. This will import the Ambox and
    mbox templates, as well as their dependencies.
5.  Now, if you go back and refresh the Template:Cleanup page you
    created, you should see the icon and a nice message box:

![cleanup message box](/GFX/mw_cleanup.png)

Finally, add the template and category pages for update and deprecated:  
  
`Template:Update`

~~~~{.text}
[[Image:Warning.png]]

'''This page is in need of updating. Some information on it may be out of date, and should not be relied on.'''

[[Category:Pages Needing Updates]]
~~~~

`Category:Pages Needing Updates`

~~~~{.text}
__HIDDENCAT__

This category keeps track of pages that need changes or updates.

'''To add pages to this category''', include the following at the '''TOP''' of the page:

{{update}}
~~~~

`Template:Deprecated`

~~~~{.text}
[[Image:Critical.png]]

'''The information on this page is badly out-of-date.''' It describes a system that is no longer in production or has drastically changed, and '''needs to be updated or rewritten'''.

[[Category:Deprecated Content]]
~~~~

`Category:Deprecated Content`

~~~~{.text}
 __HIDDENCAT__

This category keeps track of pages that are '''seriously old''' or otherwise describe systems/hosts/etc. that have seriously changed from what is described in the page.

'''To add pages to this category''', include the following at the '''TOP''' of the page:

{{deprecated}}
~~~~

And the download the two images -
[http://upload.wikimedia.org/wikipedia/commons/9/98/Ambox\_deletion.png](http://upload.wikimedia.org/wikipedia/commons/9/98/Ambox_deletion.png)
gets uploaded as Critical.png and
[http://upload.wikimedia.org/wikipedia/en/f/f4/Ambox\_content.png](http://upload.wikimedia.org/wikipedia/en/f/f4/Ambox_content.png)
gets uploaded as Warning.png.

That's it. To use this, just add `{{cleanup}}`, `{{deprecated}}` or
`{{update}}` to the top of a wiki article (adding the HTML comment
before it is also recommended), and it will add the page to the
appropriate category and show a nice message box at the top of the
page:  
  
Cleanup:  
  
![cleanup message box](/GFX/mw_cleanup.png)  
  
Update:  
  
![update message box](/GFX/mw_update.png)  
  
Deprecated:  
  
![deprecated message box](/GFX/mw_deprecated.png)

I also add a link to the top of the main wiki page:

~~~~{.text}
Things that need to be done: [[:Category:Pages Needing Updates|Pages Needing Updates]], [[:Category:Deprecated Content|Pages with Largely Deprecated Content]], [[:Category:Pages Needing Cleanup|Pages Needing Cleanup]], [[Special:WantedPages|Links to Nonexistent Pages]]
~~~~


