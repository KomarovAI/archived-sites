# 📚 Archived Sites

Automated archive of crawled websites exported from Kestra/Dagster workflows. Each site stored in separate directory with full page data, components, and link structure.

## 🌐 View Archive

**[Open GitHub Pages Archive →](https://komarovai.github.io/archived-sites/)**

## 📊 Available Sites

### 🏠 Medley HVAC (Carrollton, TX)
- **URL**: https://callmedley.com
- **Pages**: 50
- **Components**: 401
- **Links**: 6,378
- **Data Location**: `/data/medley_hvac_full_v2/`

#### Download Data
- [📄 Pages CSV](data/medley_hvac_full_v2/pages_20251214_180613.csv)
- [🧩 Components CSV](data/medley_hvac_full_v2/components_20251214_180613.csv)
- [🔗 Structure CSV](data/medley_hvac_full_v2/structure_20251214_180613.csv)

## 🛠️ Technical Details

- **Scraper**: Kestra Workflow Engine
- **Data Processing**: Dagster
- **Database**: PostgreSQL
- **Export**: GitHub API
- **Format**: CSV

## 📁 Directory Structure

```
archived-sites/
├── data/
│   ├── medley_hvac_full_v2/
│   │   ├── pages_*.csv
│   │   ├── components_*.csv
│   │   └── structure_*.csv
│   └── [other sites]/
├── index.html
└── README.md
```

## 📝 CSV Format

### Pages
- `url` - Page URL
- `title` - Page title
- `meta_description` - Meta description

### Components
- `page_url` - Source page
- `component_type` - HTML tag type
- `text_content` - Text content
- `extracted_data` - JSON data
- `position_index` - Position on page

### Structure
- `page_url` - Source page
- `linked_to_url` - Target URL
- `link_text` - Link anchor text

## ⚙️ Automated Updates

New sites are automatically added via GitHub Actions workflow when pushed to this repository.

---

**Last Updated**: December 14, 2025
