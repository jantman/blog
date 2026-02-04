# 001 - Core Pelican and Dependencies Upgrade

You must read, understand, and follow all instructions in `./README.md` when planning and implementing this feature.

## Overview

Upgrade Pelican from 3.7.1 to the latest 4.x release and update all Python dependencies in `requirements.txt` to current, Python 3-compatible versions. This includes updating `pelicanconf.py` and `publishconf.py` for any deprecated or changed settings (e.g. feed URL format strings changed from `%s` to `{slug}`), removing packages that are no longer needed or have been deprecated (e.g. `pycrypto`, `six`, `anyjson`), and ensuring the site builds successfully on a modern Python 3 interpreter.

## Status: COMPLETED

## Implementation Notes

### Environment
- Python 3.14.2 via pyenv
- Pelican 4.11.0.post0

### Changes Made

**requirements.txt** — stripped to direct build dependencies only:
- `pelican[markdown]==4.11.0.post0`
- `typogrify`
- All transitive deps (Jinja2, Markdown, Pygments, etc.) handled by pip
- Removed 20+ packages (Python 2 compat, dev tools, deployment tools, unused)

**pelicanconf.py:**
- Removed `from __future__ import unicode_literals`
- Added `RSS_FEED_SUMMARY_ONLY = False` (preserve full-content RSS feeds)
- Replaced broken `i18n_subsites` plugin with local `i18n_null` plugin
- Added `plugins` to `PLUGIN_PATHS`

**publishconf.py:**
- Removed `from __future__ import unicode_literals`
- Changed feed URLs from `%s` to `{slug}` format

**plugins/i18n_null.py** (new):
- Minimal plugin that installs null (pass-through) translations for Jinja2 i18n extension
- Replaces `i18n_subsites` which is incompatible with Pelican 4.x (references removed `Draft` class)

**pelican-bootstrap3 theme (external):**
- Fixed `base.html` feed link tags: changed `|format(category.slug)` to `.format(slug=category.slug)` for Pelican 4.x `{slug}` feed URL compatibility

### Runtime dependency
- `pytz` must be installed separately (required by sitemap plugin, not a pelican dep)

### Issues Deferred to Later Features
- Full theme migration to Pelican 4.x compatible theme (feature 002)
- Full plugin migration from monorepo to namespace plugins (feature 003)
- Minor UI differences from theme/Pelican version mismatch (feature 002)
