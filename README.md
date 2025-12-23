# Archived Sites Repository

**GitHub Pages Deployment Target** for [web-crawler](https://github.com/KomarovAI/web-crawler)

## Branches

- **`main`** → Configuration, documentation, and metadata
- **`gh-pages`** → Deployed static websites (auto-updated via workflow)

## Deployment Flow

```mermaid
web-crawler (download-site.yml)
    ↓
    [artifact: site-archive-RUN_ID]
    ↓
archived-sites (deploy-pages.yml)
    ↓
    gh-pages branch
    ↓
https://KomarovAI.github.io/archived-sites/
```

## How It Works

1. **Source Workflow** (`web-crawler`): Downloads website, creates artifact
2. **Deploy Workflow** (`archived-sites`): 
   - Receives artifact from source run
   - Creates orphan `gh-pages` branch
   - Copies files to gh-pages
   - Cleans WARC files
   - Rewrites URLs to local paths
   - Force pushes to `gh-pages`
3. **GitHub Pages**: Automatically serves `gh-pages` branch

## Configuration

### `.gitignore`
Excludes temporary and build files from git tracking.

### `.github/workflows/`
Contains GitHub Actions workflows for deployment automation.

## Access

- **Live Site**: https://KomarovAI.github.io/archived-sites/
- **Repository**: https://github.com/KomarovAI/archived-sites
- **Main Branch**: Configuration and documentation
- **GH-Pages Branch**: Active site content

## Latest Updates

- ✅ Deployed: `example.com` (2025-12-23)
- ✅ Files: 39 | Size: 1.2M
- ✅ Status: Active

## Maintenance

All deployments are automated. New sites are added via source workflow runs.

For manual updates, push to `gh-pages` branch using force update:
```bash
git push origin gh-pages --force
```

---

*Automated archive of crawled websites. Each deployment creates a fresh orphan branch.*
