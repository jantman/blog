# 001 - Core Pelican and Dependencies Upgrade

You must read, understand, and follow all instructions in `./README.md` when planning and implementing this feature.

## Overview

Upgrade Pelican from 3.7.1 to the latest 4.x release and update all Python dependencies in `requirements.txt` to current, Python 3-compatible versions. This includes updating `pelicanconf.py` and `publishconf.py` for any deprecated or changed settings (e.g. feed URL format strings changed from `%s` to `{slug}`), removing packages that are no longer needed or have been deprecated (e.g. `pycrypto`, `six`, `anyjson`), and ensuring the site builds successfully on a modern Python 3 interpreter.
