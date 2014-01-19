#!/usr/bin/env python

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import remote

import time
import os

os.environ['DISPLAY'] = ":0"

browser = webdriver.Firefox() # Get local session of firefox

def loadPages(browser, windows, one, two):
    """
    load pages, one in each window
    """
    browser.switch_to_window(windows[0])
    browser.get(one)
    browser.switch_to_window(windows[1])
    browser.get(two)
    return True

browser.get("http://www.google.com")

temp = browser.find_element_by_tag_name('body')
temp.send_keys(Keys.CONTROL, 'n')

windows = browser.window_handles

loadPages(browser, windows, 'http://localhost/blog/output/index.html', 'http://localhost/blog/output/2013/01/fedora-linux-and-osx-dual-boot-on-mid-2010-62-15-macbook-pro-laptop/')
