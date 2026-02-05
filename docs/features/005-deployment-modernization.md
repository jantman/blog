# 005 - Deployment Modernization

You must read, understand, and follow all instructions in `./README.md` when planning and implementing this feature.

## Overview

Replace the current manual deployment workflow (`ghp-import` output directory then `git push origin gh-pages`) with a GitHub Actions CI/CD pipeline that automatically builds and deploys the site to GitHub Pages on push to the main branch. This also replaces the need for local installation of `ghp-import` and ensures consistent, reproducible builds. Also replace the brittle HTML scraping in `_update_pinned_repos` with GitHub's GraphQL API.

## Implementation Plan

### Milestone 1: Create GitHub Actions CI/CD Workflow

1. Create `.github/workflows/deploy.yml` with build and deploy jobs
2. Build job: checkout, setup Python 3.14, install deps, fetch pinned repos via `gh api graphql`, run pelican, upload artifact
3. Deploy job: deploy to GitHub Pages (only on push to master)
4. Update feature doc, commit

### Milestone 2: Clean Up Local Tooling

1. Replace `_update_pinned_repos` HTML scraper with GitHub GraphQL API via `requests`
2. Remove `ghp-import` and `beautifulsoup4` from `requirements.txt`
3. Remove `publish` task from `tasks.py`
4. Verify local build, update feature doc, commit

### Milestone 3: Acceptance Criteria

1. Verify CI pipeline (push triggers build+deploy, PR triggers build only)
2. Move feature doc to `docs/features/completed/`
3. Final commit

## Progress

### Milestone 1: COMPLETE

- Created `.github/workflows/deploy.yml` with:
  - Triggers on push to `master` and PRs targeting `master`
  - Permissions: `contents: read`, `pages: write`, `id-token: write`
  - Concurrency group `pages`, cancel-in-progress only for PRs
  - Build job: checkout, Python 3.14, pip install, fetch pinned repos via `gh api graphql`, pelican build, upload artifact (push only), configure pages (push only)
  - Deploy job: runs only on push to master, deploys to `github-pages` environment
