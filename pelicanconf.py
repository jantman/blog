#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

#
# Overall site-wide settings
#
AUTHOR = u'Jason Antman'
SITENAME = u"Jason Antman's Blog"
#SITESUBTITLE = u"Subtitle here"
DISQUS_SITENAME = 'jantman'
GOOGLE_ANALYTICS_UNIVERSAL = 'UA-2718127-2'
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'jasonantman.com'

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
PAGE_PATHS = ['pages']
PAGE_EXCLUDES = []
ARTICLE_PATHS = ['content']
ARTICLE_EXCLUDES = ['pages',]

STATIC_PATHS = [
    'CNAME',
    'GFX',
    'static/favicon.ico',
    'static/robots.txt',
    'static/googleea75ea27535d4ffe.html',
]
EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'},
    'static/robots.txt': {'path': 'robots.txt'},
    'static/googleea75ea27535d4ffe.html': {'path': 'googleea75ea27535d4ffe.html'},
}

# URL settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = 'categories/{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tags/{slug}/index.html'
TAG_SAVE_AS = TAG_URL
TAGS_URL = 'tags.html'
TAGS_SAVE_AS = TAGS_URL

WITH_FUTURE_DATES = True # draft status for anything with future date

TYPOGRIFY = True
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'guess_lang': False,
            'pygments_style': 'friendly',
            'css_class': 'highlight'
        },
        'markdown.extensions.fenced_code': {},
        'markdown.extensions.toc': {}
    },
    'output_format': 'html5'
}

#
# Feeds
#
FEED_ALL_ATOM = None # TODO
CATEGORY_FEED_ATOM = None # TODO

#
# Theme and Display Settings
#
THEME = '/home/jantman/GIT/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
THEME_BRANCH = 'jantman-bootstrap3'
PYGMENTS_STYLE = 'default'

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 5

USE_OPEN_GRAPH = True

# disable tags, since it's a list not a "cloud"
DISPLAY_TAGS_ON_SIDEBAR = False

#
# Links, Social, etc.
#

LINKS =  (('Homepage', 'http://www.jasonantman.com'),
          ('Resume', 'http://resume.jasonantman.com'),)

GITHUB_URL = 'https://github.com/jantman/blog'
SHOW_GITHUB_RIBBON = True
GITHUB_USER = 'jantman'
GITHUB_SHOW_USER_LINK = True
if os.path.exists('github_pinned_repos.json'):
    with open('github_pinned_repos.json', 'r') as fh:
        GITHUB_REPOS_JSON = fh.read().strip()

TWITTER_USERNAME = 'j_antman'
TWITTER_WIDGET_ID = '429640274453594113'

#
# Plugins
#
PLUGINS = ['sitemap', 'i18n_subsites']
PLUGIN_PATHS = ['/home/jantman/GIT/pelican-plugins']
PLUGIN_BRANCH = 'jantman'
#W3C_SLEEP = 0
W3C_VALIDATOR_URL = 'http://localhost/w3c-validator/check'

I18N_TEMPLATES_LANG = 'en'
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.1
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
