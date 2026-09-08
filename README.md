# 📱 CafeBazaar Review Scraper

An automated web data collection pipeline for discovering applications and extracting user reviews from CafeBazaar.

**Discover • Crawl • Extract • Clean • Export**

---

## 🚀 Overview

CafeBazaar Review Scraper is a Python-based data collection pipeline designed to discover applications from CafeBazaar search results and transform user reviews into structured datasets.

The system automatically navigates application search results, visits individual application pages, expands dynamically loaded reviews, extracts review metadata, removes duplicate records, and exports the final dataset to Excel.

The project was designed for Persian-language application review analysis and can serve as a data acquisition layer for downstream NLP, sentiment analysis, customer feedback analysis, and market intelligence workflows.

> **Note**
>
> This repository contains a limited public demonstration of the project.
> The complete production scraping engine, platform-specific selectors,
> pagination logic, and automation routines are maintained privately.

---

## ✨ Key Features

- 🔎 Automated application discovery
- 📄 Multi-page search result crawling
- 📱 Individual application navigation
- 💬 Automated user review collection
- 🔄 Dynamic "Load More Reviews" handling
- 👤 Username extraction
- 📅 Review date extraction
- 📝 Review text extraction
- 🔗 Application URL collection
- 🧹 Duplicate review removal
- 💾 Incremental data persistence
- 📊 Structured Pandas DataFrames
- 📥 Excel export
- 🌐 Browser automation with Playwright
- 🖥️ Automatic local Chrome detection

---

## 🧠 How It Works

```text
CafeBazaar Search
       │
       ▼
Application Discovery
       │
       ▼
Collect Application URLs
       │
       ▼
Open Individual Applications
       │
       ▼
Locate User Reviews
       │
       ▼
Expand Dynamic Reviews
       │
       ▼
Extract Review Metadata
       │
       ▼
Clean & Deduplicate
       │
       ▼
Pandas DataFrame
       │
       ▼
Excel Dataset
