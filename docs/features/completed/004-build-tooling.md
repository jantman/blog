# 004 - Build Tooling Replacement

You must read, understand, and follow all instructions in `./README.md` when planning and implementing this feature.

## Overview

Replace the `fabfile.py` (Fabric 1.8.1, Python 2 only) and `develop_server.sh` with a Python 3-compatible build/task runner. The fabfile contains Python 2 syntax (`print` statements, `xrange`) and Fabric 1.x API calls that are incompatible with Python 3. All current tasks (build, clean, serve, preview, publish, post scaffolding, draft listing, category validation, and pinned repos update) need to be preserved in the replacement.

## Implementation Plan

Replace `fabfile.py` and `develop_server.sh` with a Python 3 `tasks.py` using Invoke (the direct successor to Fabric 1.x).

### Key Migration Mappings

- `from fabric.api import *` -> `from invoke import task`
- `local('...')` -> `c.run('...')`
- `local('...', capture=True)` -> `c.run('...', hide=True).stdout`
- `prompt('...')` -> `input('...')`
- `print x` -> `print(x)`
- `xrange` -> `range`
- `SimpleHTTPServer` -> `http.server`
- `env.deploy_path` -> `DEPLOY_PATH` variable
- `develop_server.sh` -> `pelican --listen --autoreload -s pelicanconf.py`

### Tasks preserved in tasks.py

12 user-facing tasks: `clean`, `build`, `rebuild`, `regenerate`, `serve`, `devserver`, `reserve`, `preview`, `publish`, `post`, `drafts`, `categories`

6 private helpers: `_make_slug`, `_prompt_title`, `_prompt_category`, `_get_categories`, `_prebuild`, `_update_pinned_repos`

### Milestones

#### Milestone 1: Create tasks.py and add dependencies

1. Create feature branch `feature/004-build-tooling`
2. Add `invoke`, `beautifulsoup4`, `requests`, `ghp-import` to `requirements.txt`
3. Create `tasks.py` with all tasks migrated from fabfile.py
4. Verify: `inv --list` shows all 12 tasks, `inv clean`, `inv build`, `inv categories`, `inv drafts` all work
5. Update feature doc, commit, build/serve for human review, open PR

#### Milestone 2: Remove legacy files and acceptance criteria

1. `git rm fabfile.py develop_server.sh`
2. Verify build still works: `inv build`, `inv devserver`
3. Final checklist: all 12 tasks work, no old file references remain
4. Move feature doc to `docs/features/completed/`
5. Commit, update PR

## Progress

### Milestone 1: COMPLETE

- Created feature branch `feature/004-build-tooling`
- Added `invoke`, `beautifulsoup4`, `requests`, `ghp-import` to `requirements.txt`
- Created `tasks.py` with all 12 tasks and 6 private helpers migrated from `fabfile.py`
- All Python 2 syntax replaced with Python 3 equivalents
- Added non-interactive mode handling for `_update_pinned_repos` (accepts automatically when stdin is not a TTY)
- Added empty-result guard for pinned repos scraping (HTML selectors may be stale)
- `develop_server.sh` replaced by `inv devserver` using `pelican --listen --autoreload`
- Verified: `inv --list` (12 tasks), `inv clean`, `inv build` (394 articles), `inv categories`, `inv drafts` all work

### Milestone 2: COMPLETE

- Removed `fabfile.py` and `develop_server.sh` via `git rm`
- Verified `inv build` still works (394 articles processed)
- Blog visually confirmed rendering correctly at http://localhost:8000
- Feature doc moved to `docs/features/completed/`
