from fabric.api import *
import fabric.contrib.project as project
import os
import re
import datetime

from pelicanconf import ARTICLE_DIR, DEFAULT_CATEGORY, AUTHOR

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
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

def cf_upload():
    rebuild()
    local('cd {deploy_path} && '
          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          '-U {cloudfiles_username} '
          '-K {cloudfiles_api_key} '
          'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )

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

def post():
    """ write a post """
    title = _prompt_title()
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
Category: {defaultcat}
Tags: 
Slug: {slug}
Summary: <<<<< summary goes here >>>>>>>
Status: draft

content (written in MarkDown - http://daringfireball.net/projects/markdown/syntax )
""".format(title=title,
           datestr=datestr,
           defaultcat=DEFAULT_CATEGORY,
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
