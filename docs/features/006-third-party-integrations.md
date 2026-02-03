# 006 - Third-Party Integration Cleanup

You must read, understand, and follow all instructions in `./README.md` when planning and implementing this feature.

## Overview

Several third-party service integrations configured in the blog are defunct or obsolete and need to be updated or removed. Google Analytics is configured with a Universal Analytics property (`UA-` prefix) which has been sunset in favor of GA4. The Shariff social sharing buttons include Google+, which no longer exists. The Twitter widget and username references may need updating given the platform's rebrand. Disqus comment integration should be reviewed for current compatibility. Each integration should be evaluated and either updated to its current equivalent or removed.
