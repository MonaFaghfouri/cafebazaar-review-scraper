# 📱 CafeBazaar Review Scraper

An automated data collection pipeline for discovering applications and extracting user reviews from CafeBazaar.

**Discover • Crawl • Extract • Clean • Export**

---

## 🚀 Overview

**CafeBazaar Review Scraper** is a Python-based web data collection pipeline designed to discover applications from CafeBazaar search results and transform user reviews into structured datasets.

The system automatically navigates search result pages, identifies relevant applications, visits individual application pages, loads dynamically available user reviews, extracts review metadata, removes duplicate records, and exports the final dataset to Excel.

The project is particularly suitable for collecting Persian-language application reviews and creating datasets for downstream tasks such as **sentiment analysis, customer feedback analysis, topic modeling, NLP research, and market intelligence**.

> **Note**
>
> This repository contains a limited public demonstration of the project.
> The complete production scraping engine, platform-specific selectors,
> pagination logic, review-loading implementation, and automation routines
> are maintained privately.

---

## ✨ Key Features

* 🔎 Automated application discovery
* 📄 Multi-page search result crawling
* 📱 Individual application navigation
* 💬 Automated user review collection
* 🔄 Dynamic review loading
* 👤 Username extraction
* 📅 Review date extraction
* 📝 Review text extraction
* 🔗 Application URL collection
* 🧹 Duplicate record removal
* 💾 Incremental data saving
* 📊 Structured data processing with Pandas
* 📥 Automated Excel export
* 🌐 Browser automation with Playwright
* 🖥️ Automatic local Google Chrome detection
* 🇮🇷 Support for Persian-language content

---

## 🧠 How It Works

```text
          Search Keyword
                │
                ▼
       CafeBazaar Search
                │
                ▼
      Application Discovery
                │
                ▼
    Collect Application URLs
                │
                ▼
    Open Individual App Pages
                │
                ▼
       Locate User Reviews
                │
                ▼
    Load Dynamically Available
             Reviews
                │
                ▼
       Extract Metadata
                │
                ▼
      Clean & Deduplicate
                │
                ▼
       Pandas DataFrame
                │
                ▼
          Excel Export
```

---

## 🔎 Application Discovery

The pipeline begins with a search keyword.

For example:

```text
Insurance
```

or its Persian equivalent:

```text
بیمه
```

The scraper navigates through CafeBazaar search result pages and automatically collects application URLs returned for the selected query.

The discovered applications are then processed individually.

This makes it possible to move from a simple search term to a structured collection of application-level review data.

---

## 💬 Review Collection Workflow

For every discovered application, the production pipeline performs the following workflow:

```text
Open Application Page
          │
          ▼
Identify Application
          │
          ▼
Locate Review Section
          │
          ▼
Load Additional Reviews
          │
          ▼
Continue Review Expansion
          │
          ▼
Extract Review Records
          │
          ▼
Validate & Clean Data
          │
          ▼
Add to Dataset
```

Because review content can be loaded dynamically, browser automation is used to interact with the page and access additional publicly available review records.

---

## 📊 Dataset Structure

The generated dataset contains structured review-level information.

| Field           | Description                        |
| --------------- | ---------------------------------- |
| Application     | Name of the CafeBazaar application |
| Username        | Review author username             |
| Review Date     | Review publication date            |
| Review Text     | User-submitted review              |
| Application URL | URL of the application page        |

Example:

| Application          | Username | Review Date | Review Text                               |
| -------------------- | -------- | ----------- | ----------------------------------------- |
| Sample Insurance App | User123  | 1405/06/10  | Sample review for demonstration purposes. |

The resulting structure can be directly used for further analysis in Python, Excel, Power BI, or NLP pipelines.

---

## 🛠️ Tech Stack

| Technology          | Usage                              |
| ------------------- | ---------------------------------- |
| Python              | Core application                   |
| Playwright          | Browser automation                 |
| Pandas              | Data processing and transformation |
| OpenPyXL            | Excel generation and formatting    |
| Google Chrome       | Browser execution                  |
| Regular Expressions | Review metadata parsing            |

---

## 🌐 Browser Automation

CafeBazaar contains dynamically rendered content that may require browser interaction.

The production pipeline therefore uses:

```text
Playwright
     │
     ▼
Google Chrome
     │
     ▼
CafeBazaar
     │
     ▼
Dynamic Content
     │
     ▼
Review Extraction
```

The application can detect a locally installed Google Chrome browser and launch it through Playwright.

This design avoids depending exclusively on a separately downloaded browser runtime and makes the scraper easier to execute in supported local environments.

---

## 🔄 Dynamic Review Loading

User reviews may not all be available in the initial page state.

The production scraper handles dynamic review expansion by interacting with the review section and continuing to request additional publicly available reviews.

Conceptually:

```text
Initial Reviews
      │
      ▼
Additional Reviews Available?
      │
   ┌──┴──┐
   │     │
  Yes    No
   │     │
   ▼     ▼
Load    Finish
More
   │
   └──────────────► Repeat
```

The exact selectors and production review-expansion implementation are intentionally excluded from the public repository.

---

## 🧹 Data Processing

Raw review information is transformed into a consistent structured format before export.

The processing pipeline includes:

```text
Raw Review Data
       │
       ▼
Field Extraction
       │
       ▼
Text Cleaning
       │
       ▼
Record Validation
       │
       ▼
Duplicate Removal
       │
       ▼
Structured DataFrame
```

Duplicate records are removed before generating the final dataset.

---

## 💾 Incremental Data Persistence

Large review collection jobs can run for extended periods.

Network interruptions, browser failures, or manual termination could otherwise result in losing previously collected data.

The production implementation therefore supports incremental persistence while applications are being processed.

```text
Application 1
     │
     ▼
Collect Reviews
     │
     ▼
Save Progress
     │
     ▼
Application 2
     │
     ▼
Collect Reviews
     │
     ▼
Save Progress
     │
     ▼
     ...
```

This design reduces the risk of losing already collected records during long-running data acquisition tasks.

---

## 📥 Excel Export

Collected reviews are exported into a structured Excel workbook.

The export process includes:

* structured column names
* duplicate removal
* readable column widths
* wrapped review text
* worksheet filtering
* frozen headers
* right-to-left worksheet support where appropriate

This makes the resulting dataset immediately usable for manual inspection and further analysis.

---

## 📁 Repository Structure

```text
cafebazaar-review-scraper/
│
├── README.md
├── demo_scraper.py
├── requirements.txt
├── .gitignore
├── sample_reviews.xlsx
│
└── screenshots/
    ├── search.png
    ├── scraping.png
    └── output.png
```

---

## 🎯 Public Demo vs Production Version

This repository is intentionally designed as a **technical showcase**.

### Included in the Public Repository

* Project architecture
* Technology stack
* Demonstration processing logic
* Example workflow
* Sample review dataset
* Screenshots
* Dataset structure
* Documentation

### Not Publicly Distributed

The production implementation contains additional components including:

* platform-specific scraping selectors
* complete application discovery logic
* search pagination implementation
* complete review expansion logic
* production browser automation routines
* extraction heuristics
* failure recovery mechanisms
* production-specific optimization
* internal scraping workflow

These components are intentionally maintained separately.

---

## 🔐 Source Availability

The complete production source code is **not open source**.

This repository is provided for:

* portfolio demonstration
* technical evaluation
* data engineering showcase
* web automation demonstration
* research and academic applications
* recruitment purposes

Production implementation details remain private.

---

## 💡 Potential Applications

Structured application review datasets can support several analytical and research applications.

### 🧠 Sentiment Analysis

Review text can be classified into positive, neutral, and negative sentiment.

```text
Reviews
   ↓
Persian NLP
   ↓
Sentiment Classification
   ↓
Customer Satisfaction Analysis
```

### 🏷️ Topic Modeling

Large collections of reviews can be analyzed to discover recurring customer concerns and themes.

Potential approaches include:

* LDA
* BERTopic
* embedding-based clustering
* transformer-based topic extraction

### 📊 Customer Feedback Analytics

Reviews can be transformed into actionable customer intelligence such as:

* common complaints
* frequently requested features
* usability problems
* service quality issues
* application performance problems

### 🏢 Competitive Intelligence

Reviews from multiple applications within the same market can be compared to identify differences in customer experience and satisfaction.

### 📈 Temporal Analysis

Because review dates are collected, future analytical pipelines can examine changes in customer feedback over time.

---

## 🧩 Example Analytical Pipeline

The scraper can serve as the data acquisition layer of a larger analytics system:

```text
             CafeBazaar
                 │
                 ▼
          Review Scraper
                 │
                 ▼
        Structured Dataset
                 │
        ┌────────┼─────────┐
        │        │         │
        ▼        ▼         ▼
   Sentiment   Topic     Complaint
   Analysis   Modeling   Detection
        │        │         │
        └────────┼─────────┘
                 ▼
        Customer Insights
                 │
                 ▼
       Dashboard / Reports
```

---

## 💡 Engineering Challenges

Some of the main engineering challenges addressed by this project include:

* processing JavaScript-rendered content
* navigating multiple search result pages
* automatically discovering application URLs
* interacting with dynamically loaded review sections
* processing Persian-language text
* detecting Persian-formatted review dates
* preventing duplicate records
* handling long-running browser automation tasks
* preserving collected data during execution
* producing clean and analysis-ready Excel outputs

---

## 🗺️ Future Development

Potential future extensions include:

* 🧠 Persian sentiment analysis
* 🏷️ automatic review topic classification
* 🤖 LLM-based review summarization
* 📊 interactive analytics dashboard
* 📈 temporal sentiment tracking
* 🚨 negative-review monitoring
* 🔔 automated complaint alerts
* 🗄️ database-backed review storage
* 🔍 application comparison
* ⚡ parallelized data collection
* 📊 Power BI integration
* 🌐 Streamlit-based user interface

---

## ⚙️ Installation

Install the required Python packages:

```bash
pip install playwright pandas openpyxl
```

The production version is designed to work with a locally installed Google Chrome browser.

---

## 🧪 Public Demo

The `demo_scraper.py` file included in this repository demonstrates the public-facing data processing structure of the project.

It does **not** contain the complete production scraping engine.

Example:

```python
import pandas as pd

sample_data = [
    {
        "Application": "Sample Insurance App",
        "Username": "User123",
        "Review Date": "1405/06/10",
        "Review Text": "Sample review for demonstration purposes.",
        "Application URL": "https://cafebazaar.ir/app/example",
    }
]

df = pd.DataFrame(sample_data)

print(df)
```

---

## ⚠️ Responsible Use

This project is intended for educational, research, portfolio, and data engineering demonstration purposes.

Users of web scraping and browser automation technologies are responsible for complying with:

* applicable website terms of service
* robots policies
* access restrictions
* privacy requirements
* applicable laws and regulations

The project should only be used to access information that users are authorized to collect.

---

## 👩‍💻 Author

**Mona Faghfouri Azar**

Data Analytics • Artificial Intelligence • Automation • Web Data Engineering

GitHub: **MonaFaghfouri**

---

## 📌 Related Project

**Price Intelligence Platform**

A multi-source product search and price intelligence system integrating web scraping, browser automation, data normalization, and Excel export.

---

**Python • Playwright • Pandas • Web Scraping • Browser Automation • Data Engineering • Persian NLP**

© 2026 Mona Faghfouri Azar. All rights reserved.
