# 002 - Theme Migration

You must read, understand, and follow all instructions in `./README.md` when planning and implementing this feature.

## Overview

The blog currently uses a custom fork of the `pelican-bootstrap3` theme located outside this repository at `/home/jantman/GIT/pelican-themes/pelican-bootstrap3` on a custom `jantman-bootstrap3` branch. This theme needs to be vendored into this repository and updated for Pelican 4.x template compatibility. The goal is to preserve the existing visual appearance (Bootstrap 3 Flatly theme) while fixing any Jinja2 template incompatibilities introduced by the Pelican 4.x upgrade; a full Bootstrap version upgrade is explicitly out of scope.

## Implementation Plan

### Key Technical Context

- The pelican-themes repo is a monorepo containing 100+ themes. `pelican-bootstrap3` is a regular directory (not submodule).
- Must use `git subtree split` to extract just the pelican-bootstrap3 subdirectory before adding it.
- The `jantman-bootstrap3` branch is 1 commit ahead of origin (needs push first).
- `fabfile.py` imports `THEME_BRANCH` and validates the external theme's git branch — must be updated.
- `os` is already imported in `pelicanconf.py`.
- Templates are already Pelican 4.x compatible — no template changes needed.

### Milestone 1: Vendor Theme via Git Subtree (prefix: `Theme Migration - 1`)

**Task 1.1: Push unpushed theme commit**
Push the 1 unpushed commit on `jantman-bootstrap3` in `/home/jantman/GIT/pelican-themes` to origin.

**Task 1.2: Create subtree split branch**
In `/home/jantman/GIT/pelican-themes`:
```bash
git subtree split --prefix=pelican-bootstrap3 jantman-bootstrap3 -b pelican-bootstrap3-split
```

**Task 1.3: Add theme to blog repo via git subtree**
In `/home/jantman/GIT/blog`:
```bash
git remote add pelican-themes /home/jantman/GIT/pelican-themes
git fetch pelican-themes pelican-bootstrap3-split
git subtree add --prefix=theme --squash pelican-themes/pelican-bootstrap3-split
```

**Task 1.4: Update `pelicanconf.py`**
- Change `THEME` to use computed local path: `THEME = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'theme')`
- Remove `THEME_BRANCH = 'jantman-bootstrap3'`

**Task 1.5: Update `fabfile.py`**
- Remove `THEME_BRANCH` from the import
- Remove the git branch validation block (keep the directory existence check)

**Task 1.6: Build verification**
- Run `pelican -s pelicanconf.py` and verify clean build
- Start local server for visual review

**Task 1.7: Update feature doc, commit, request human visual review**

### Milestone 2: Acceptance Criteria (prefix: `Theme Migration - 2`)

**Task 2.1: Final verification checklist**
- Clean build with no errors
- `theme/templates/base.html` and `theme/static/` exist in repo
- `pelicanconf.py` uses computed local THEME path
- Human has visually confirmed the blog renders correctly

**Task 2.2: Move feature doc to completed**
```bash
git mv docs/features/002-theme-migration.md docs/features/completed/
```

**Task 2.3: Final commit and PR**
- Commit with prefix `Theme Migration - 2`
- Open GitHub PR to merge `feature/001-core-pelican-upgrade` → `master`

### Critical Files

| File | Change |
|------|--------|
| `pelicanconf.py:94,96` | Update THEME path, remove THEME_BRANCH |
| `fabfile.py:15,38-41` | Remove THEME_BRANCH import and git branch check |
| `docs/features/002-theme-migration.md` | Update with plan/progress, then move to completed/ |
| `theme/` (new) | Vendored theme via git subtree |

### Verification

1. `pelican -s pelicanconf.py` exits 0 with no template errors
2. `ls theme/templates/base.html` exists
3. `python -m http.server 8000` in output/ — human visual review
4. `git log --oneline -5` shows subtree merge commit

## Progress

- [ ] Milestone 1: Vendor Theme via Git Subtree
- [ ] Milestone 2: Acceptance Criteria
