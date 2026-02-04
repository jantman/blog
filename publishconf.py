#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://blog.jasonantman.com'
RELATIVE_URLS = False

# TODO - update feedburner? see http://docs.getpelican.com/en/3.3.0/settings.html#feedburner
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/feed.atom.xml'
FEED_RSS = 'feeds/feed.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/categories/{slug}.atom.xml'
CATEGORY_FEED_RSS = 'feeds/categories/{slug}.rss.xml'
TAG_FEED_ATOM = 'feeds/tags/{slug}.atom.xml'
TAG_FEED_RSS = 'feeds/tags/{slug}.rss.xml'
FEED_MAX_ITEMS = 50

DELETE_OUTPUT_DIRECTORY = True
