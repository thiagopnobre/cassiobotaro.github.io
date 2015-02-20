#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'C\xe1ssio Botaro'
SITENAME = u'import None'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'
THEME = 'pelican-bootstrap3'
DISQUS_SITENAME = 'importnone'

STATIC_PATHS = ('images', 'static')
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (
    (
        'twitter',
        'http://twitter.com/cassiobotaro'
    ),
    (
        'linkedin',
        'http://br.linkedin.com/pub/c%C3%A1ssio-botaro/b1/43/6a2'
    )
)
OUTPUT_PATH = '../output'
GITHUB_USER = 'cassiobotaro'
GITHUB_REPO_COUNT = 3
ABOUT_ME = "WebDeveloper at Diarios Associados. "\
           "UHlzc2lvbmF0ZSB3ZWJkZXZlbG9wZXIuCg=="
AVATAR = 'http://www.gravatar.com/avatar/'\
         'a19c2dcbc9fc6ae1c340528186320d9c?s=100'
GOOGLE_ANALYTICS = 'UA-59964005-1'

DEFAULT_PAGINATION = 10
ADDTHIS_PROFILE = 'ra-54023148366c6bdd'
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True
BOOTSTRAP_THEME = 'superhero'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
