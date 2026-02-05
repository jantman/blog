"""
Invoke tasks for building and managing the Pelican blog.

Replaces the legacy fabfile.py (Fabric 1.x / Python 2).
Usage: inv --list
"""

import os
import re
import sys
import stat
import json
import time
import datetime
from pprint import pformat

from invoke import task
import requests

from pelicanconf import (
    ARTICLE_PATHS, DEFAULT_CATEGORY, AUTHOR, OUTPUT_PATH, THEME,
    GITHUB_USER, MENUITEMS
)

DEPLOY_PATH = OUTPUT_PATH.rstrip('/')


def _make_slug(title):
    """Make a URL slug from the given title."""
    slug = title.lower()
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'[^A-Za-z0-9_-]', '', slug)
    return slug


def _prompt_title():
    """Prompt for a post title with confirmation."""
    confirm = 'no'
    while not re.match(r'(y|Y|yes|Yes|YES)', confirm):
        title = input("Post Title: ")
        print("")
        print("Post Title: '%s'" % title)
        print("Slug: '%s'" % _make_slug(title))
        print("")
        confirm = input("Is this correct? [y|N] ") or 'no'
    return title


def _prompt_category(cats):
    """Prompt for a category selection."""
    print("\n\nSelect a Category:\n==================")
    for i in range(len(cats)):
        print("%d) %s" % (i, cats[i]))
    print("")
    confirm = 'no'
    while not re.match(r'(y|Y|yes|Yes|YES)', confirm):
        category = input("Category (number or free text): ")
        print("")
        if re.match(r'[0-9]+', category):
            idx = int(category)
            if 0 <= idx < len(cats):
                category = cats[idx]
            else:
                print("Invalid number.")
                continue
        print("Category: '%s'" % category)
        print("")
        confirm = input("Is this correct? [y|N] ") or 'no'
    return category


def _get_categories(c):
    """Return a list of all categories in current posts."""
    result = c.run(
        'grep -rh "^Category: " %s/ | sort | uniq' % ARTICLE_PATHS[0],
        hide=True
    )
    cats = []
    cat_re = re.compile(r'^Category: (.+)$')
    for line in result.stdout.split("\n"):
        m = cat_re.match(line)
        if not m:
            continue
        cats.append(m.group(1))
    return cats


def _prebuild(c):
    """Tasks to run before any file generation."""
    if not os.path.exists(THEME):
        print("ERROR: theme directory %s does not exist." % THEME)
        sys.exit(1)
    cats = _get_categories(c)
    mitems = [x[0] for x in MENUITEMS]
    missing = [i for i in cats if i not in mitems]
    if len(missing) > 0:
        raise RuntimeError(
            'Categories missing from MENUITEMS in pelicanconf.py: %s' % missing
        )
    _update_pinned_repos()


def _update_pinned_repos():
    """Update github_pinned_repos.json from user's GitHub profile via GraphQL API."""
    if not os.path.exists('github_pinned_repos.json'):
        fage = 999999999
    else:
        fage = time.time() - os.stat('github_pinned_repos.json')[stat.ST_MTIME]
    if fage < 86400:
        print(
            "GitHub Pinned Repos updated %d seconds ago; not regenerating"
            % fage
        )
        return True
    print("Updating GitHub Pinned Repos for user %s" % GITHUB_USER)
    query = """
    {
      user(login: "%s") {
        pinnedItems(first: 6, types: REPOSITORY) {
          nodes {
            ... on Repository {
              name
              url
              description
            }
          }
        }
      }
    }
    """ % GITHUB_USER
    token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
    if not token:
        print("WARNING: GITHUB_TOKEN or GH_TOKEN not set. "
              "GitHub GraphQL API requires authentication. Skipping update.")
        return False
    headers = {'Authorization': 'bearer %s' % token}
    r = requests.post(
        'https://api.github.com/graphql',
        json={'query': query},
        headers=headers
    )
    r.raise_for_status()
    data = r.json()
    if 'errors' in data:
        print("WARNING: GraphQL errors: %s. Skipping update." % data['errors'])
        return False
    nodes = data.get('data', {}).get('user', {}).get('pinnedItems', {}).get('nodes', [])
    result = [
        {
            'name': node['name'],
            'html_url': node['url'],
            'description': node.get('description', '') or ''
        }
        for node in nodes
    ]
    if not result:
        print("WARNING: No pinned repos found. Skipping update.")
        return False
    res = json.dumps(result)
    print("New pinned repos:\n%s" % pformat(result))
    if sys.stdin.isatty():
        resp = input("Is this right? [yes|No] ")
        if not re.match(r'(y|Y|yes|Yes|YES)', resp):
            return False
    else:
        print("Non-interactive mode: accepting pinned repos update.")
    with open('github_pinned_repos.json', 'w') as fh:
        fh.write(res)
    return True


@task
def clean(c):
    """Remove output directory and recreate it."""
    if os.path.isdir(DEPLOY_PATH):
        c.run('rm -rf %s' % DEPLOY_PATH)
        c.run('mkdir %s' % DEPLOY_PATH)


@task
def build(c):
    """Run pelican to build output."""
    _prebuild(c)
    c.run('pelican -s pelicanconf.py')


@task
def rebuild(c):
    """Clean and build."""
    clean(c)
    build(c)


@task
def regenerate(c):
    """Regenerate whenever a file changes (pelican -r)."""
    _prebuild(c)
    c.run('pelican -r -s pelicanconf.py')


@task
def serve(c):
    """Start HTTP server in output directory."""
    c.run('cd %s && python -m http.server' % DEPLOY_PATH)


@task
def devserver(c):
    """Start Pelican dev server with live reload on port 8000."""
    _prebuild(c)
    c.run('pelican --listen --autoreload -s pelicanconf.py')


@task
def reserve(c):
    """Build and serve."""
    build(c)
    serve(c)


@task
def preview(c):
    """Build with publishconf.py settings."""
    _prebuild(c)
    c.run('pelican -s publishconf.py')


@task
def post(c):
    """Scaffold a new blog post."""
    cats = _get_categories(c)
    title = _prompt_title()
    category = _prompt_category(cats)
    dt = datetime.datetime.now()
    dname = os.path.join(ARTICLE_PATHS[0], dt.strftime('%Y'), dt.strftime('%m'))
    if not os.path.exists(dname):
        os.makedirs(dname)
    slug = _make_slug(title)
    fname = "%s.md" % slug
    fpath = os.path.join(dname, fname)
    datestr = dt.strftime('%Y-%m-%d %H:%M')
    metadata = """Title: {title}
Date: {datestr}
Modified: {datestr}
Author: {author}
Category: {category}
Tags:
Slug: {slug}
Summary: <<<<< summary goes here >>>>>>>
Status: draft

<!--- remove this next line to disable Table of Contents -->
[TOC]
""".format(title=title,
           datestr=datestr,
           category=category,
           slug=slug,
           author=AUTHOR)
    with open(fpath, 'w') as fh:
        fh.write(metadata)
        fh.flush()
        os.fsync(fh.fileno())
    if os.environ.get('EDITOR') is None:
        print("EDITOR not defined. Your post is started at: %s" % fpath)
    else:
        editor = os.environ.get('EDITOR')
        print("Replacing process with: %s %s" % (editor, os.path.abspath(fpath)))
        os.execlp(editor, os.path.basename(editor), os.path.abspath(fpath))


@task
def drafts(c):
    """List draft posts."""
    c.run(
        'grep -rl -e "^Status: draft" -e "^:status: draft" content/'
        ' | grep -v "~$"',
        warn=True
    )


@task
def categories(c):
    """Show all current blog post categories."""
    for cat in _get_categories(c):
        print(cat)
