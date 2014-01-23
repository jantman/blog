#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#
# Overall site-wide settings
#
AUTHOR = u'Jason Antman'
SITENAME = u"Jason Antman's Blog"
SITESUBTITLE = u"Subtitle here"
#DISQUS_SITENAME = None
#GOOGLE_ANALYTICS = 'UA-XXXX-YYYY'
SITEURL = '' # TODO

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 10
# PAGINATION_PATTERNS - TODO

DEFAULT_CATEGORY = "Miscellaneous"

#
# Content / Files
#
IGNORE_FILES = ['.#*']

# PATH = 'content/'
PAGE_DIR = 'pages'
PAGE_EXCLUDES = []
ARTICLE_DIR = 'content'
ARTICLE_EXCLUDES = ['pages',]
STATIC_PATHS = ['images', 'GFX', 'favicon.ico']

# URL settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_URL = 'tags.html'
TAGS_SAVE_AS = TAGS_URL

WITH_FUTURE_DATES = True # draft status for anything with future date

TYPOGRIFY = True
MD_EXTENSIONS = ['codehilite(guess_lang=False)', 'fenced_code', 'toc']

#
# Feeds
#
FEED_ALL_ATOM = None # TODO
CATEGORY_FEED_ATOM = None # TODO
"""
# TODO - update feedburner? see http://docs.getpelican.com/en/3.3.0/settings.html#feedburner
FEED_DOMAIN = None # TODO - should be SITEURL
FEED_ATOM = None # TODO
FEED_RSS = None # TODO
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'
"""


#
# Theme and Display Settings
#
THEME = 'themes/pelican-bootstrap3'

DISPLAY_CATEGORIES_ON_MENU = True

TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 25

#MENUITEMS = None
# list of tuples (Title, URL) to displat at beginning of main menu

#
# Links, Social, etc.
#

LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

GITHUB_URL = 'https://github.com/jantman'

TWITTER_USERNAME = 'j_antman'

#
# Plugins
#
PLUGINS = []
# TODO - https://github.com/getpelican/pelican-plugins
