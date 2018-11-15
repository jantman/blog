Title: Puppet Syntax Highlighting with GeSHi
Date: 2012-01-11 12:32
Author: admin
Category: Software
Tags: GeSHi, mediawiki, PHP, puppet, wordpress
Slug: puppet-syntax-highlighting-with-geshi

This blog is run on wordpress, and I also do quite a bit in PHP, so I'm
familiar with the [GeSHi](http://qbnz.com/highlighter/) syntax
highlighter. It's PHP-based, and can run both as a Wordpress plugin
([WP-Syntax](http://wordpress.org/extend/plugins/wp-syntax/)) and as a
PHP module. It also works quite well with the MediaWiki [SyntaxHighlight
GeSHi](http://www.mediawiki.org/wiki/Extension:SyntaxHighlight_GeSHi)
extension.

Today I was documenting some [Puppet](http://www.puppet.org) code in a
wiki, and realized that I didn't have syntax highlighting. Well, fellow
Linux sysadmin and puppetmaster Jason Hancock was nice enough to post on
his blog ([Puppet Syntax Highlighting with
GeSHi](http://geek.jasonhancock.com/2011/10/14/puppet-syntax-highlighting-geshi/))
that he's developed a GeSHi language file for Puppet, available from
[GitHub](https://github.com/jasonhancock/geshi-language-files). Many
thanks!
