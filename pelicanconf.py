#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"James Mills"
AUTHOR_EMAIL = "prologic@shortcircuit.net.au"
SITENAME = u"Circuits Framework"
SITEURL = ""

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

PATH = "content"

THEME = "theme"
BOOTSTRAP_THEME = "cerulean"

TIMEZONE = "Australia/Brisbane"

DEFAULT_LANG = u"en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = "{date:%Y}/{date:%b}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html"
CATEGORY_URL = "{slug}/"
CATEGORY_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ("Home", "/"),
    ("Downloads", "/downloads"),
    ("Docs", "/docs"),
    ("Blogs", "/blogs"),
    ("Community", "/community"),
    ("Support", "/support"),
)

# Blogroll
LINKS = (
    ("PyPi", "https://pypi.python.org/pypi/circuits"),
    ("Github", "https://github.com/circuits/circuits"),
    ("Waffle",  "https://waffle.io/circuits/circuits"),
    ("OpenHub", "https://www.openhub.net/p/circuits"),
    ("Coveralls", "https://coveralls.io/r/circuits/circuits"),
    ("Landscape", "https://landscape.io/github/circuits/circuits"),
    ("Travis CI", "https://travis-ci.org/circuits/circuits"),
    ("ReadTheDocs", "http://circuits.readthedocs.org/"),
)

# Social widget
SOCIAL = (
    ("Github", "https://github.com/circuits"),
    ("Twitter", "https://twitter.com/pythoncircuits")
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGINS = (
    "sitemap",
    "headerid",
    "code_include",
    "filetime_from_git",
    "html_rst_directive",
    "twitter_bootstrap_rst_directives",
)
