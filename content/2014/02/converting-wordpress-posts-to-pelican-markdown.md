Title: Converting WordPress Posts to Pelican MarkDown
Date: 2014-02-28 22:21
Tags: pelican,wordpress,blog,markdown
Category: Miscellaneous
Slug: converting-wordpress-posts-to-pelican-markdown
Author: Jason Antman
Summary: My adventures converting my WordPress blog to Pelican, the problems I encountered, and how I solved them.

A few weeks ago, I
[posted](/2014/01/planning-migration-from-wordpress-to-static-site/) about my
plans to convert my self-hosted WordPress blog to a static site using a static
blog generator. Since then, I've decided to stop working on my exhaustive
[static blog generator comparison spreadsheet](https://docs.google.com/spreadsheet/ccc?key=0AnHh-ye5DNiNdF9DWkJrT2kzSkNsNVp6cjMzLXJ6VEE&usp=sharing)
and just try [Pelican](http://getpelican.com) - mainly because it's written in
Python which is my current strongest language, comes highly recommended, seems
to have most of the features I want, and seems to be easily extensible.

So, I walked through the documentation for the latest version (3.3.0), started
a [GitHub repo](https://github.com/jantman/blog), and tweaked a bunch of
settings. The repo is public, so if you want to take a look behind the scenes,
see my [fabfile](https://github.com/jantman/blog/blob/master/fabfile.py),
etc. feel free. 

## Initial WordPress Import Attempt

I used the WordPress XML Export tool, as instructed in the [Pelican Importer documentation](http://docs.getpelican.com/en/latest/importer.html).
At first, I attempted to do a more-or-less default import from WordPress using
the `pelican-import` tool, which writes rST, and then build the blog. What I
ended up with was thousands of errors complaining about "Inline interpreted
text or phrase reference start-string without end-string", "Explicit markup
ends without a blank line; unexpected uninden", "malformed hyperlink target",
"Unknown target name" on all of my links, and a bevy of other Docutils
errors. It was so utterly awful that I gave up.

## WordPress Import as MarkDown

Next I tried importing as MarkDown instead of rST, using:

````
pelican-import --markup markdown --wpfile -o content/ --dir-page jasonantman039sblog.wordpress.2014-01-11.xml
````

That built without errors, and the posts looked somewhat right out of the
box, without any of the previous thousands of errors. And the links looked
mostly right - even the captions for images. Though I'm working at a Python
shop and writing a lot of Python these days, my knowledge of MarkDown is still
much better than rST, so this is fine for me. (I even wrote a `fab post` task
that prompts for a title, generates all of the post metadata, writes it to the
right file, and opens up an editor on it.)

The first problem was that the import script gave me one "content" directory
with 346 ".md" files in it - not exactly easy to work with. Luckily the
metadata was right, so a quick little
[bash script](https://github.com/jantman/blog/blob/master/move_wordpress.sh)
moved the posts into a YYYY/MM directory hierarchy.

## Obvious Problems with Imported Posts

After getting the MarkDown import working, and the posts moved to the proper
paths, I was still having some issues...

### Syntax Hilighting Gone

In WordPress, I was using the
[WP-Syntax](http://wordpress.org/extend/plugins/wp-syntax/) plugin to perform
syntax hilighting via [GeSHi](http://qbnz.com/highlighter/). The plugin uses
pre tags with a `lang=` attribute to specify the language, like:

````
<pre lang="bash">
````

Unfortunately, these translated to some really ugly MarkDown fenced blocks like:

    ~~~~ {lang="bash"}
    cp /boot/efi/EFI/fedora/grub.cfg /boot/efi/EFI/fedora/grub.cfg.bak
    echo 'GRUB_DISABLE_OS_PROBER="true"' >> /etc/default/grub
    grub2-mkconfig > /boot/efi/EFI/fedora/grub.cfg
    ~~~~

that seem to be just a bit off from what MarkDown/Pygments can handle. The
places where I just used bare `<pre>` blocks translated fine.

http://blog.gastove.com/2013-09-17_enabling_line_numbers_for_pygments.html

Fixed this by using fenced blocks with the 'lang=' stuff removed, and in class
syntax like the MarkDown docs suggest. Some four-tab-indents with
:::identifier work.

### Broken Links

It seems that something in the conversion process introduced line wraps (could
it really be Pandoc itself???) Unfortunately, this wreaks havoc with any
explicit reference links
that use long (long enough to break across lines) titles, depending on where
they are in the line. It seems that in some places they end up breaking
differently in the link in the text and in the link definition, which MarkDown misses, and
then renders broken links and plain text of the link table at the bottom of
the page. Manually removing the line breaks and any extraneous spaces seems to
fix it.

So, yes, Pandoc was doing this because of the `--reference-links` parameter
that `pelican-import` was calling it with. There was an
[issue](https://github.com/getpelican/pelican/issues/348) and
[pull request](https://github.com/getpelican/pelican/pull/642) to fix this,
but when I started with Pelican the last release was 3.3.0 (4 months ago) and
the PR was merged after that. So, if you're having the same problem and the
latest release of Pelican is still 3.3.0, you might as well just apply
[the patch](https://github.com/getpelican/pelican/commit/83e4d35b44a422ee8d4b077f505970d03e555f45)
yourself - it's just a very simple removal of a parameter in
`pelican_import.py`.

## Overall Results

I'm quite happy with the overall results. I also spent a *lot* of time manually fixing
markup issues that didn't translate well through Pandoc, but I suppose that's to be
expected given that many of my older blog posts had HTML issues.
