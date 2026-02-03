# 002 - Theme Migration

You must read, understand, and follow all instructions in `./README.md` when planning and implementing this feature.

## Overview

The blog currently uses a custom fork of the `pelican-bootstrap3` theme located outside this repository at `/home/jantman/GIT/pelican-themes/pelican-bootstrap3` on a custom `jantman-bootstrap3` branch. This theme needs to be vendored into this repository and updated for Pelican 4.x template compatibility. The goal is to preserve the existing visual appearance (Bootstrap 3 Flatly theme) while fixing any Jinja2 template incompatibilities introduced by the Pelican 4.x upgrade; a full Bootstrap version upgrade is explicitly out of scope.
