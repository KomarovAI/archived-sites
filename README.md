# Archived Sites

Automated archive of crawled websites exported from Kestra workflows.

## Structure

Each website is stored in its own directory:

```
archived-sites/
├── site1/
│   ├── index.html
│   ├── page1.html
│   ├── page2.html
│   └── assets/
│       ├── images/
│       ├── css/
│       └── js/
├── site2/
│   ├── index.html
│   └── ...
└── site3/
    └── ...
```

## Workflow

1. **Crawler**: `full-site-crawler` workflow crawls websites → saves to PostgreSQL
2. **Export**: `db-to-github-export` workflow exports from PostgreSQL → pushes to this repo

## Automation

- Commits are automated by Kestra workflow
- Each export creates commit: `Auto-export site {name} from DB [{timestamp}]`
- Sites are versioned through Git history

## Source

Exported from: [kestra-docker-starter](https://github.com/KomarovAI/kestra-docker-starter)

## Usage

Browse any site directory to view archived HTML files. All sites are static and can be:
- Viewed directly in GitHub
- Downloaded for offline browsing
- Deployed to static hosting (GitHub Pages, Netlify, etc.)

## Privacy

🔒 This repository is **private**. Only authorized users can access archived sites.
