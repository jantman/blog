from fabric.api import *
import fabric.contrib.project as project
import os
import re
import datetime

from pelicanconf import ARTICLE_DIR, DEFAULT_CATEGORY, AUTHOR, OUTPUT_PATH

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'


def clean():
    """ remove DEPLOY_PATH if it exists, then recreate """
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    """ run pelican to build output """
    local('pelican -s pelicanconf.py')

def rebuild():
    """ clean and build """
    clean()
    build()

def regenerate():
    """ pelican -r ; regenerate whenever a file changes """
    local('pelican -r -s pelicanconf.py')

def serve():
    """ SimpleHTTPServer """
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    """ build and serve """
    build()
    serve()

def preview():
    """ pelican with publishconf.py """
    local('pelican -s publishconf.py')

def publish():
    """ rebuild and publish to GH pages """
    resp = prompt("This will clean, build, and push to GH pages. Ok? [yes|No]")
    if not re.match(r'(y|Y|yes|Yes|YES)', resp):
        return False
    clean()
    local('pelican -s publishconf.py')
    local("ghp-import %s" % OUTPUT_PATH)
    local("git push origin gh-pages")

def _make_slug(title):
    """ make a slug from the given title """
    slug = title.lower()
    slug = re.sub('\s+', '-', slug)
    slug = re.sub(r'[^A-Za-z0-9_-]', '', slug)
    return slug

def _prompt_title():
    """ prompt for a post title """
    confirm = 'no'
    while not re.match(r'(y|Y|yes|Yes|YES)', confirm):
        title = prompt("Post Title:")
        print("")
        print("Post Title: '%s'" % title)
        print("Slug: '%s'" % _make_slug(title))
        print("")
        confirm = prompt("Is this correct? [y|N]", default='no')
    return title

def drafts():
    """ list drafts """
    local('grep -rl -e "^Status: draft" -e "^:status: draft" content/ | grep -v "~$"')

def _prompt_category(cats):
    """ prompt for a category selection """
    print("\n\nSelect a Category:\n==================")
    for c in xrange(0, len(cats)):
        print("%d) %s" % (c, cats[c]))
    print("")
    confirm = 'no'
    while not re.match(r'(y|Y|yes|Yes|YES)', confirm):
        category = prompt("Category (number or free text):")
        print("")
        if re.match(r'[0-9]+', category):
            foo = int(category)
            if foo in xrange(0, len(cats)):
                category = cats[foo]
            else:
                print("Invalid number.")
                continue
        print("Category: '%s'" % category)
        print("")
        confirm = prompt("Is this correct? [y|N]", default='no')
    return category

def post():
    """ write a post """
    cats = _get_categories()
    title = _prompt_title()
    category = _prompt_category(cats)
    dt = datetime.datetime.now()
    dname = os.path.join(ARTICLE_DIR, dt.strftime('%Y'), dt.strftime('%m'))
    if not os.path.exists(dname):
        os.makedirs(dname)
    slug = _make_slug(title)
    fname = "%s.md" % slug
    fpath = os.path.join(dname, fname)
    datestr = dt.strftime('%Y-%m-%d %H:%M')
    metadata = """Title: {title}
Date: {datestr}
Author: {author}
Category: {category}
Tags: 
Slug: {slug}
Summary: <<<<< summary goes here >>>>>>>
Status: draft

content (written in MarkDown - http://daringfireball.net/projects/markdown/syntax )
""".format(title=title,
           datestr=datestr,
           category=category,
           slug=slug,
           author=AUTHOR)
    with open(fpath, 'w') as fh:
        fh.write(metadata)
        # need to flush and fsync before an exec
        fh.flush()
        os.fsync(fh.fileno())
    if os.environ.get('EDITOR') is None:
        print("EDITOR not defined. Your post is started at: %s" % fpath)
    else:
        editor = os.environ.get('EDITOR')
        print("Replacing fab process with: %s %s" % (editor, os.path.abspath(fpath)))
        # replace our process with the editor...
        os.execlp(editor, os.path.basename(editor), os.path.abspath(fpath))

def _get_categories():
    """ return a list of all categories in current posts """
    lines = local('grep -rh "^Category: " %s/ | sort | uniq' % ARTICLE_DIR, capture=True)
    cats = []
    cat_re = re.compile(r'^Category: (.+)$')
    for l in str(lines).split("\n"):
        m = cat_re.match(l)
        if not m:
            continue
        cats.append(m.group(1))
    return cats

def categories():
    """ show all current blog post categories """
    for c in _get_categories():
        print c

def submodules():
    """ update all git submodules """
    print("Still needs to be implemented")
    # GitPython 0.3.2 provides repo.git.version_info(), as we need 1.8.2+ to
    # have submodules track branches - http://bec-systems.com/site/1020/git-submodules-can-now-track-branches
