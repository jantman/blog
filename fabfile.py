from fabric.api import local

import os
import sys

venv = os.getenv("VIRTUAL_ENV", None)
if venv is None:
    sys.stderr.write("ERROR: fab must be run from within a venv. Activate venv first.\n")
    sys.exit(2)

def build():
    local("pelican content/")

def deploy():
    print("Not implemented.")
    return False

