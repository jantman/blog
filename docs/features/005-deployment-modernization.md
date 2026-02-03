# 005 - Deployment Modernization

You must read, understand, and follow all instructions in `./README.md` when planning and implementing this feature.

## Overview

Replace the current manual deployment workflow (`ghp-import` output directory then `git push origin gh-pages`) with a GitHub Actions CI/CD pipeline that automatically builds and deploys the site to GitHub Pages on push to the main branch. This also replaces the need for local installation of `ghp-import` and ensures consistent, reproducible builds.
