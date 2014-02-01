#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#
# Overall site-wide settings
#
AUTHOR = u'Jason Antman'
SITENAME = u"Jason Antman's Blog"
#SITESUBTITLE = u"Subtitle here"
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
OUTPUT_PATH = 'output/'

IGNORE_FILES = ['.#*']

# PATH = 'content/'
PAGE_DIR = 'pages'
PAGE_EXCLUDES = []
ARTICLE_DIR = 'content'
ARTICLE_EXCLUDES = ['pages',]
STATIC_PATHS = ['images', 'GFX', 'favicon.ico', 'CNAME', 'robots.txt']

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
THEME = '/home/jantman/GIT/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
THEME_BRANCH = 'jantman-bootstrap3'

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 5

# disable tags, since it's a list not a "cloud"
DISPLAY_TAGS_ON_SIDEBAR = True
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 20
#MENUITEMS = [('Tags', '/tags.html')]

#MENUITEMS = None
# list of tuples (Title, URL) to displat at beginning of main menu

#
# Links, Social, etc.
#

LINKS =  (('Homepage', 'http://www.jasonantman.com'),
          ('Resume', 'http://resume.jasonantman.com'),)

#SOCIAL = (('@j_antman', 'http://twitter.com/j_antman'),)

GITHUB_URL = 'https://github.com/jantman/blog'
SHOW_GITHUB_RIBBON = True
GITHUB_USER = 'jantman'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = False
GITHUB_SHOW_USER_LINK = True

TWITTER_USERNAME = 'j_antman'
TWITTER_WIDGET_ID = '429640274453594113'

#ADDTHIS_PROFILE = ''

#
# Plugins
#
PLUGINS = []
PLUGIN_PATH = '/home/jantman/GIT/pelican-plugins'
PLUGIN_BRANCH = 'jantman'
