Title: Custom MediaWiki Sidebar; New Blog?
Date: 2008-06-18 22:26
Author: admin
Category: Projects
Tags: blog, firefox, mediawiki, PHP
Slug: custom-mediawiki-sidebar-new-blog

As you may have noticed, some [Firefox
3](http://www.spreadfirefox.com/node&id=238326&t=305)
[buttons](http://www.spreadfirefox.com/?q=affiliates/homepage) have
popped up not only here on my blog, but also on my
[wiki](http://www.jasonantman.com/). While adding the buttons to
[Blogger](http://www.blogger.com/) was a simple addition to the
template, getting them in the sidebar of MediaWiki wasn't exactly as
easy (yeah, I'm considering the arduous project of moving my whole 102+
page wiki to [Drupal](http://drupal.org/) or another good F/OSS CMS).

After some serious grepping through the source, and adding HTML comments
to see where they appeared, I finally found a solution to add the button
to the MediaWiki sidebar - though I'd really like it to appear below the
search box (I guess that's something for my to-do list). I'm using the
MonoBook skin (though somewhat modified). I'm using "MonoBook nouveau",
and it should be the version that shipped with MW 1.10.1. In this
version, I added the code around line 166. Specifically, this was added
before the `<div id="p-search" class="portlet">` line, and after the end
of the `foreach ($this->data['sidebar'] as $bar => $cont)` loop. This
threw the button in a box directly above the search box, and below all
of my sidebar links.

The code looked something like:

~~~~{.html}
<?php } ?>
<!-- firefox link added to MonoBook.php by jantman 2008-06-18 -->
<div class='portlet' id='p-logos'>
<h5>Cool Stuff</h5>
<div class='pBody'>
<ul>
<li><a href="http://www.spreadfirefox.com/node&id=238326&t=305" target="_blank">
<img border="0" alt="Firefox 3" title="Firefox 3" src="http://sfx-images.mozilla.org/affiliates/Buttons/firefox3/110x32_best-yet.png"/>
</a>
</li>
</ul>
</div>
</div>
<!-- end firefox link -->
<div id="p-search" class="portlet">
~~~~

In other news, I'm taking a Data Driven Websites class this summer
(PHP/MySQL, but for some reason they switched to a Windows server...
endless problems, and I can't even edit with Nano on the server, let
alone emacs). Our first project was to build a blog engine, which I'm
working on right now. Anyway, it got me thinking... the one thing that
Blogger is missing is the ability to post to a given category, and allow
users to view or subscribe to a specific category (or everything). So I
think I may look into writing something like that myself, if I can't
find a good alternative that's already done and is F/OSS. Regardless,
I'll probably be keeping the Blogger template as well as (ugh) moving
over all of my current posts, which Blogger chose to store in raw HTML.
So there's going to be a lot of parsing on my future...

PS - When I get a new blog engine, I'm also going to go for a slightly
modified template that uses relative widths and placement - so that
code, like the snippet here, fits the screen correctly.
