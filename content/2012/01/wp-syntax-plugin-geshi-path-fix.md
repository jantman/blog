Title: WP-Syntax Plugin GeSHi Path Fix
Date: 2012-01-12 19:09
Author: admin
Category: Tech HowTos
Tags: GeSHi, PHP, syntax highlighting, wordpress
Slug: wp-syntax-plugin-geshi-path-fix

The [Wp-Syntax](http://wordpress.org/extend/plugins/wp-syntax/) plugin
for [WordPress](http://wordpress.org) provides syntax highlighting for
WordPress blogs via the [GeSHi](http://qbnz.com/highlighter) PHP syntax
highlighter. Unfortunately, the plugin includes a builtin version of
GeSHi (currently 1.0.8.9) in `geshi/`. As a result, not only are users
of the plugin not instructed to use the latest version of GeSHi, but it
won't use a host-wide GeSHi installation that's already in the PHP
include path (i.e. `/usr/share/php/`), like the the many [php-geshi
packages](http://pkgs.org/search/?keyword=php-geshi&search_on=name&distro=0&arch=32-bit)
offered by repositories including
[EPEL](http://fedoraproject.org/wiki/EPEL) (for Fedora, CentOS and
RHEL).

The fix is quite simple. Just open `wp-syntax.php` in the `wp-syntax/`
plugin directory in your favorite text editor and change the GeSHi
include line (for WP-Syntax 0.9.12, this is line 53) from:

~~~~{.php}
include_once("geshi/geshi.php");
~~~~

to:

~~~~{.php}
include_once("geshi.php");
~~~~

If you already have GeSHi installed in the PHP include path, just remove
the `geshi` directory in your `wp-syntax/` plugin directory, flush the
WordPress caches (if any), and load a page which uses GeSHi - it should
now use the host-wide version. If you want to still use a local version
for wp-syntax, you can move things around to where they *should* be in
the `wp-syntax/` plugin directory:

~~~~{.bash}
mv geshi/geshi.php . && mv geshi/geshi/* geshi/ && rmdir geshi/geshi
~~~~

Note - if you're in a shared hosting environment, or are otherwise not
able to upgrade the php-geshi package on your server yourself, you might
not want to do this.

I also [posted about this in the WordPress support
forums](http://wordpress.org/support/topic/wp-syntax-move-geshi-include-path-to-allow-use-with-host-wide-geshi?replies=1#post-2556903).
Hopefully the WP-Syntax devs will include this change in the next
version...
