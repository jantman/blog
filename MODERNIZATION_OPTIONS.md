# Blog Modernization Options

**Date:** February 2026
**Current Stack:** Pelican 3.7.1 (Python 2.7 era) with Bootstrap 3 theme

## Executive Summary

This blog uses a decade-old Pelican setup with Python 2-era dependencies that need modernization. The primary goals are:
- Update to actively maintained software with security patches
- Maintain current URL structure (`YYYY/MM/slug/`)
- Minimize visual and functional changes
- Simplify the build/deployment process

## Current Technical Debt

| Component | Current Version | Status |
|-----------|-----------------|--------|
| Pelican | 3.7.1 | Outdated (current: 4.11.0) |
| Python | 2.7 era code | End of life since 2020 |
| Fabric | 1.8.1 | Python 2 only, no longer maintained |
| pycrypto | 2.6.1 | Deprecated, security concerns |
| Bootstrap | 3.x | End of life (current: 5.x) |
| Markdown | 2.3.1 | Very outdated |

---

## Ranked Modernization Options

### 1. Upgrade Pelican to 4.x (Recommended)

**Effort:** Low-Medium | **Risk:** Low | **Disruption:** Minimal

This approach keeps the existing architecture while modernizing all components.

#### What Changes
- Pelican 3.7.1 → 4.11.0 (Python 3.10+ required)
- Replace Fabric 1.x with Invoke (modern task runner from same author)
- Update theme to [bootstrap-next](https://github.com/shvchk/bootstrap-next) (Bootstrap 4) or update custom theme
- Update all Python dependencies to current versions
- Replace `develop_server.sh` with `pelican --listen`

#### Breaking Changes to Address
- URL settings now use `{slug}` instead of `%s` (yours already uses correct format)
- Theme templates need `TAG_FEED_ATOM.format(slug=tag.slug)` instead of `TAG_FEED_ATOM|format(tag.slug)`
- RSS feeds default to summary-only (set `RSS_FEED_SUMMARY_ONLY = False` to keep current behavior)
- `develop_server.sh` replaced with built-in `pelican --listen`

#### Migration Steps
1. Create Python 3.11+ virtual environment
2. Install `pelican[markdown]==4.11.0` and updated dependencies
3. Update `pelicanconf.py` for any deprecated settings
4. Test/update custom theme for Pelican 4.x compatibility
5. Replace `fabfile.py` with `tasks.py` using Invoke
6. Update GitHub Actions/deployment workflow

#### Pros
- Preserves all customizations and content as-is
- URL structure unchanged
- Familiar Python tooling
- Smallest learning curve
- Active development ([Pelican GitHub](https://github.com/getpelican/pelican))

#### Cons
- Still using Bootstrap 3 (unless theme is also updated)
- Pelican's market share has declined
- Custom theme may need updates

#### Resources
- [Pelican 4.x Changelog](https://docs.getpelican.com/en/latest/changelog.html)
- [Pelican Documentation](https://docs.getpelican.com/)

---

### 2. Migrate to Hugo

**Effort:** Medium | **Risk:** Low-Medium | **Disruption:** Medium

Hugo is the fastest static site generator, written in Go, with excellent Pelican migration support.

#### Why Hugo
- Build times measured in milliseconds (vs. seconds for Pelican)
- Single binary with no dependencies
- Active development and large community
- [300+ themes](https://themes.gohugo.io/) available
- Built-in live reload server

#### Migration Approach
- Use [existing migration scripts](https://gist.github.com/andreagrandi/0a7bf6e217d6561b00b6a5de6211ddaa) as starting point
- Front matter conversion: Pelican → Hugo YAML format
- URL preservation via Hugo's `url` or `aliases` front matter
- Select Bootstrap-based Hugo theme (e.g., [Hugo Bootstrap Theme](https://themes.gohugo.io/themes/hugo-theme-bootstrap/))

#### URL Preservation
```yaml
# In each post's front matter
url: /2024/01/my-post/
# OR for redirects from old URLs
aliases:
  - /2024/01/my-post/
```

#### Pros
- Extremely fast builds
- No runtime dependencies (single Go binary)
- Excellent documentation
- Real-time preview with hot reload
- Strong community support

#### Cons
- Go templating has learning curve
- Need to find/adapt theme to match current look
- Front matter migration required for all posts
- Different plugin ecosystem

#### Resources
- [Hugo Migration Tools](https://gohugo.io/tools/migrations/)
- [Pelican to Hugo Migration Guide](https://arunrocks.com/moving-blogs-pelican-to-hugo/)
- [Hugo Themes](https://themes.gohugo.io/)

---

### 3. Migrate to Jekyll

**Effort:** Medium | **Risk:** Low | **Disruption:** Medium

Jekyll is the original static site generator and powers GitHub Pages natively.

#### Why Jekyll
- First-class GitHub Pages integration (zero-config deployment)
- Mature ecosystem with extensive documentation
- Similar Markdown + front matter workflow to Pelican
- Large theme selection with Bootstrap options

#### GitHub Pages Advantage
- Push to repo → automatic build and deploy
- No need for `ghp-import` or separate build step
- Free HTTPS via GitHub

#### Migration Approach
- Convert Pelican front matter to Jekyll format
- Configure `_config.yml` with matching permalink structure
- Select compatible Bootstrap theme

#### Permalink Configuration
```yaml
# _config.yml
permalink: /:year/:month/:title/
```

#### Pros
- Native GitHub Pages support
- Mature, stable platform
- Liquid templating is straightforward
- Large theme ecosystem
- Ruby is well-supported

#### Cons
- Ruby dependency (may be unfamiliar)
- Slower builds than Hugo
- Less flexible than Hugo/Eleventy
- GitHub Pages restricts some plugins

#### Resources
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Jekyll Themes](https://jekyllthemes.io/)

---

### 4. Migrate to Eleventy (11ty)

**Effort:** Medium-High | **Risk:** Medium | **Disruption:** Medium

Eleventy is a modern, flexible JavaScript-based static site generator.

#### Why Eleventy
- Zero client-side JavaScript by default
- Supports 10 template languages (including Markdown)
- Extremely flexible configuration
- Modern JavaScript ecosystem
- Fast build times

#### Migration Approach
- Export Pelican Markdown content
- Configure Eleventy collections for blog posts
- Set up permalink structure to match existing URLs
- Create or adapt Bootstrap template

#### Permalink Configuration
```javascript
// .eleventy.js
eleventyConfig.addCollection("posts", function(collectionApi) {
  return collectionApi.getFilteredByGlob("content/**/*.md");
});

// In post front matter
permalink: "/{{ date | date: '%Y/%m' }}/{{ slug }}/"
```

#### Pros
- Modern JavaScript tooling (npm ecosystem)
- Highly flexible and customizable
- Zero config to start, infinitely configurable
- Active development and community
- Fast builds

#### Cons
- Requires JavaScript/Node.js knowledge
- Smaller ecosystem than Hugo/Jekyll
- More manual configuration for blog features
- No direct Pelican migration tools

#### Resources
- [Eleventy Documentation](https://www.11ty.dev/docs/)
- [Eleventy Permalinks](https://www.11ty.dev/docs/permalinks/)

---

### 5. Migrate to Astro

**Effort:** High | **Risk:** Medium-High | **Disruption:** High

Astro is a modern web framework that can function as a static site generator with advanced capabilities.

#### Why Astro
- Ships zero JavaScript by default
- Component-based architecture
- Can integrate React/Vue/Svelte components if needed
- Excellent performance optimization
- Modern developer experience

#### Migration Approach
- Significant restructuring required
- Content collections for blog posts
- Custom components for layout
- Most complex migration of all options

#### Pros
- Most modern architecture
- Future-proof technology choices
- Component islands for interactivity
- Excellent image optimization
- Type-safe content (with TypeScript)

#### Cons
- Steepest learning curve
- Most significant departure from current setup
- Overkill for a simple blog
- Requires JavaScript/TypeScript knowledge
- No direct migration path from Pelican

#### Resources
- [Astro Documentation](https://docs.astro.build/)
- [Astro Blog Template](https://astro.build/themes/?search=&categories%5B%5D=blog)

---

## Recommendation Matrix

| Criteria | Pelican 4.x | Hugo | Jekyll | Eleventy | Astro |
|----------|-------------|------|--------|----------|-------|
| Migration Effort | Low | Medium | Medium | Medium-High | High |
| URL Preservation | Native | Easy | Easy | Manual | Manual |
| Visual Continuity | High | Medium | Medium | Medium | Low |
| Future-Proofing | Medium | High | Medium | High | High |
| Build Speed | Medium | Fastest | Slow | Fast | Fast |
| Learning Curve | None | Medium | Low | Medium | High |
| Community Size | Small | Large | Large | Medium | Growing |

## Final Recommendation

**For minimal disruption with maximum modernization: Upgrade to Pelican 4.x**

This approach:
- Requires the least content migration
- Preserves your custom theme (with minor updates)
- Maintains familiar Python tooling
- Keeps all URLs identical
- Can be done incrementally

**If you want better long-term positioning: Migrate to Hugo**

Hugo offers:
- The fastest builds
- Excellent migration documentation
- Large, active community
- No runtime dependencies
- Better long-term maintenance outlook

---

## Next Steps

1. **Decide on approach** based on time available and comfort with new tools
2. **Create a test branch** for migration experimentation
3. **Set up local development environment** for chosen platform
4. **Migrate a few posts first** to validate URL structure and styling
5. **Complete full migration** with comprehensive testing
6. **Update deployment workflow** (GitHub Actions recommended for all options)

---

## Sources

- [Pelican Documentation](https://docs.getpelican.com/)
- [Pelican GitHub Repository](https://github.com/getpelican/pelican)
- [Hugo Migration Tools](https://gohugo.io/tools/migrations/)
- [CloudCannon: Top 5 Static Site Generators for 2025](https://cloudcannon.com/blog/the-top-five-static-site-generators-for-2025-and-when-to-use-them/)
- [Kinsta: Top 5 Static Site Generators in 2026](https://kinsta.com/blog/static-site-generator/)
- [Bootstrap-next Theme](https://github.com/shvchk/bootstrap-next)
- [Pelican to Hugo Migration](https://www.andreagrandi.it/posts/migrating-from-pelican-to-hugo/)
- [Hugo Discourse: Pelican Migration](https://discourse.gohugo.io/t/pelican-blog-migration-how-to-reduce-manual-effort/52219)
