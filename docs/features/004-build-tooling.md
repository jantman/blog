# 004 - Build Tooling Replacement

You must read, understand, and follow all instructions in `./README.md` when planning and implementing this feature.

## Overview

Replace the `fabfile.py` (Fabric 1.8.1, Python 2 only) and `develop_server.sh` with a Python 3-compatible build/task runner. The fabfile contains Python 2 syntax (`print` statements, `xrange`) and Fabric 1.x API calls that are incompatible with Python 3. All current tasks (build, clean, serve, preview, publish, post scaffolding, draft listing, category validation, and pinned repos update) need to be preserved in the replacement.
