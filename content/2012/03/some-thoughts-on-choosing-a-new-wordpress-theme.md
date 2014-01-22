Title: Some Thoughts on Choosing a New Wordpress Theme
Date: 2012-03-17 11:48
Author: admin
Category: Miscellaneous
Tags: analysis, analytics, blog, google, logging, stats, theme, wordpress
Slug: some-thoughts-on-choosing-a-new-wordpress-theme

I think I'm going to choose a new theme for my blog. The current theme
is [iNove][] (albeit an older version with some custom modifications),
and I feel like it looks a bit messy and has gotten a bit cluttered, so
it's time to find something new. I like the 2-column layout, and have a
few other things I'm looking for - specifically, aside from something
with advanced features like lots of widget support and hooks, something
that has good visual separation between different posts and widgets. I
also really want something, if possible, with relative column widths. My
current home and work desktops both have dual monitors, and the minimum
resolution I have on one screen is 1920x1080. When I look at my blog in
a maximized window, about half the screen width is wasted with empty
space. So, ideally, I'd like a theme that's based on relative widths,
probably with a "min-width" property so it wouldn't get compressed to an
absurdly narrow width on small screens.

I use [Google Analytics][] (as noted in the [privacy policy][]) for
visitor statistics on this blog (more about that in a moment). So, I
took a peek at the breakdown of visitors by screen resolution, and saw
that for the past year, 94% of the 27,500 visits had a screen width of
1024px or more (and the majority of the others looked like mobile device
resolutions, so they'd probably zoom the page correctly). So, my first
gut reaction was to assume that I could use a theme approximately 1000px
wide. Unfortunately, there's two main problems with that: first, as
mentioned by [Chris Coyier on CSS-Tricks.com][], just because someone
has a given screen resolution doesn't mean their browser window (let
alone the viewport) is that size. As a matter of fact, I usually have my
main browser window set at about 80% of the width of one of my monitors,
with my instant messaging client [Pidgin][] taking up the rest of the
space. So there's one inaccuracy. There's a potentially much greater
inaccuracy in my stats as well, which I'm going to discuss in a
[separate post][].

  [iNove]: http://wordpress.org/extend/themes/inove
  [Google Analytics]: http://www.google.com/analytics/
  [privacy policy]: /privacy-policy/
  [Chris Coyier on CSS-Tricks.com]: http://css-tricks.com/screen-resolution-notequalto-browser-window/
  [Pidgin]: http://pidgin.im/
  [separate post]: /2012/03/inaccuracies-in-google-analytics-for-website-stats/
