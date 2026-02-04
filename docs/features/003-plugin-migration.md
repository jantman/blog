# 003 - Plugin Migration

You must read, understand, and follow all instructions in `./README.md` when planning and implementing this feature.

## Overview

The blog currently loads the `sitemap` and `i18n_null` plugins from a shared external monorepo at `/home/jantman/GIT/pelican-plugins` on a custom `jantman` branch. Pelican 4.x introduced a namespace plugin system where plugins are installed as standard Python packages (e.g. `pelican-sitemap`). This feature replaces the external monorepo dependency with the pip-installable `pelican-sitemap` namespace plugin package and updates configuration accordingly. The local `i18n_null` plugin stays as-is in `plugins/`.

## Implementation Plan

### Key Technical Context

- `pelicanconf.py` loaded plugins via `PLUGIN_PATHS` pointing to the external monorepo and local `plugins/` dir.
- `PLUGIN_BRANCH` was used by `fabfile.py` to validate the monorepo was on the correct git branch.
- The namespace `pelican-sitemap` package does NOT require `pytz` (unlike the old monorepo version).
- `i18n_null` is a local plugin in `plugins/` providing null translations for Jinja2 i18n; it remains unchanged.

### Milestone 1: Migrate Plugins (prefix: `Plugin Migration - 1`)

**Task 1.1: Create feature branch**
Create branch `feature/003-plugin-migration` from `master`.

**Task 1.2: Add `pelican-sitemap` to `requirements.txt`**
Add `pelican-sitemap` to `requirements.txt` and install it.

**Task 1.3: Update `pelicanconf.py`**
- Remove external monorepo path from `PLUGIN_PATHS`: change to `['plugins']`
- Remove `PLUGIN_BRANCH = 'jantman'`
- Keep `PLUGINS = ['sitemap', 'i18n_null']` unchanged

**Task 1.4: Update `fabfile.py`**
- Remove `PLUGIN_PATHS` and `PLUGIN_BRANCH` from the import
- Remove the plugin monorepo validation block in `prebuild()` (LICENSE check, branch check)

**Task 1.5: Build verification**
- Run `pelican -s pelicanconf.py` and verify clean build
- Verify `sitemap.xml` is generated in output

**Task 1.6: Update feature doc, commit, request human visual review**

### Milestone 2: Acceptance Criteria (prefix: `Plugin Migration - 2`)

**Task 2.1: Final verification checklist**
- Clean build with no errors
- `sitemap.xml` is generated in output
- `pelicanconf.py` has no references to external monorepo
- `fabfile.py` has no monorepo validation
- Human has visually confirmed the blog renders correctly

**Task 2.2: Move feature doc to completed**
```bash
git mv docs/features/003-plugin-migration.md docs/features/completed/
```

**Task 2.3: Final commit and PR**

### Critical Files

| File | Change |
|------|--------|
| `requirements.txt` | Add `pelican-sitemap` |
| `pelicanconf.py:155-157` | Remove external monorepo from PLUGIN_PATHS, remove PLUGIN_BRANCH |
| `fabfile.py:16,39-45` | Remove PLUGIN_BRANCH import and monorepo validation |
| `docs/features/003-plugin-migration.md` | Update with plan/progress, move to completed |

### Verification

1. `pip install -r requirements.txt` succeeds
2. `pelican -s pelicanconf.py` exits 0 with no errors
3. `ls output/sitemap.xml` exists
4. Visual review of blog in browser
5. No references to `/home/jantman/GIT/pelican-plugins` remain in config files

## Progress

- [x] Milestone 1: Migrate Plugins
  - [x] Task 1.1: Create feature branch (`feature/003-plugin-migration`)
  - [x] Task 1.2: Add `pelican-sitemap` to `requirements.txt` (installed v1.2.2)
  - [x] Task 1.3: Update `pelicanconf.py` (removed monorepo path, removed PLUGIN_BRANCH)
  - [x] Task 1.4: Update `fabfile.py` (removed PLUGIN_PATHS/PLUGIN_BRANCH import, removed monorepo validation)
  - [x] Task 1.5: Build verification (394 articles, no errors, sitemap.xml generated at 204KB)
  - [x] Task 1.6: Commit and human visual review
- [ ] Milestone 2: Acceptance Criteria
  - [ ] Task 2.1: Final verification checklist
  - [ ] Task 2.2: Move feature doc to completed
  - [ ] Task 2.3: Final commit and PR
