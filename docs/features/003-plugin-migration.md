# 003 - Plugin Migration

You must read, understand, and follow all instructions in `./README.md` when planning and implementing this feature.

## Overview

The blog currently loads the `sitemap` and `i18n_subsites` plugins from a shared external monorepo at `/home/jantman/GIT/pelican-plugins` on a custom `jantman` branch. Pelican 4.x introduced a namespace plugin system where plugins are installed as standard Python packages (e.g. `pelican-sitemap`). This feature replaces the external monorepo dependency with pip-installable namespace plugin packages and updates `pelicanconf.py` accordingly.
