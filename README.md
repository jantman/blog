# Jason Antman's Blog

[![Project Status: Active - The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/0.1.0/active.svg)](http://www.repostatus.org/#active)

This is the repository that backs my [Pelican](http://getpelican.com)-powered static blog. It's here for anyone to take a peek at.

## Requirements

- Python 3.14+ (recommended via [pyenv](https://github.com/pyenv/pyenv))
- A GitHub personal access token (for fetching pinned repos)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/jantman/blog.git
   cd blog
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up GitHub token for pinned repos (optional but recommended):

   ```bash
   export GITHUB_TOKEN="your_token_here"
   # or
   export GH_TOKEN="your_token_here"
   ```

## Build and Development

This project uses [Invoke](https://www.pyinvoke.org/) for task automation. List all available tasks with:

```bash
inv --list
```

### Available Tasks

| Task | Description |
|------|-------------|
| `inv build` | Build the site with Pelican |
| `inv clean` | Remove output directory and recreate it |
| `inv rebuild` | Clean and build (combines both) |
| `inv serve` | Start HTTP server in output directory (port 8000) |
| `inv devserver` | Start Pelican dev server with live reload |
| `inv reserve` | Build and serve |
| `inv regenerate` | Watch for file changes and regenerate |
| `inv preview` | Build with production settings (publishconf.py) |
| `inv post` | Scaffold a new blog post (interactive) |
| `inv drafts` | List all draft posts |
| `inv categories` | Show all current blog post categories |

### Common Workflows

**Local development with live reload:**

```bash
inv devserver
```

Then open http://localhost:8000 in your browser. The site will automatically rebuild when you edit content.

**Create a new blog post:**

```bash
inv post
```

This will interactively prompt for title and category, then create a new post file and open it in your `$EDITOR`.

**Production preview:**

```bash
inv preview
inv serve
```

## Deployment

Deployment is automated via GitHub Actions. When you push to the `master` branch:

1. GitHub Actions builds the site using `publishconf.py` settings
2. Fetches pinned GitHub repos via GraphQL API
3. Deploys to GitHub Pages

Pull requests trigger a build-only job for validation.

**Note:** The GitHub repository must have Pages configured to deploy from "GitHub Actions" (not "Deploy from a branch").

## Project Structure

```
blog/
├── content/           # Blog posts (Markdown)
├── pages/             # Static pages
├── theme/             # Vendored pelican-bootstrap3 theme (Flatly)
├── plugins/           # Local Pelican plugins
│   └── i18n_null.py   # Null translations for Jinja2 i18n
├── output/            # Generated site (git-ignored)
├── pelicanconf.py     # Development configuration
├── publishconf.py     # Production configuration
├── tasks.py           # Invoke tasks
├── requirements.txt   # Python dependencies
└── .github/workflows/ # CI/CD configuration
```

## Configuration

### Pelican

- `pelicanconf.py` - Development settings (relative URLs, etc.)
- `publishconf.py` - Production settings (absolute URLs, feeds enabled)

### Theme

The blog uses a vendored fork of [pelican-bootstrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3) with the Bootstrap 3 Flatly theme. The theme is located in the `theme/` directory.

### Plugins

- **sitemap** - Installed via pip (`pelican-sitemap`), generates `sitemap.xml`
- **i18n_null** - Local plugin in `plugins/`, provides null translations for Jinja2 i18n extension

### Third-Party Integrations

- **Google Analytics 4** - Configured via `GOOGLE_ANALYTICS` in `pelicanconf.py`
- **Disqus Comments** - Configured via `DISQUS_SITENAME` in `pelicanconf.py`
- **Shariff Social Sharing** - Privacy-friendly sharing buttons (Facebook, LinkedIn, Diaspora)
- **GitHub Pinned Repos** - Sidebar widget showing pinned GitHub repositories

## Dependencies

See `requirements.txt`:

- `pelican[markdown]==4.11.0.post0` - Static site generator with Markdown support
- `pelican-sitemap` - Sitemap generation plugin
- `typogrify` - Typography enhancements
- `invoke` - Task runner
- `requests` - HTTP client (for GitHub API)

## License

Content is my own; see individual posts for licensing. Code/configuration is provided as-is for reference.
