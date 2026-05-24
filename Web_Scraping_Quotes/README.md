# Web Scraping Quotes Project

## Overview

This project is a simple web scraping application built using Python.
It scrapes quotes data from the website:

[Quotes to Scrape](https://quotes.toscrape.com?utm_source=chatgpt.com)

The scraper collects:

* Quote
* Author
* Author Link
* Tags

The scraped data is stored in a CSV file.

---

## Technologies Used

* Python
* Requests
* BeautifulSoup
* CSV

---

## Project Files

```text id="y3x6ur"
Web_Scraping_Quotes/
│── quotes_scrape.py
│── quotes.csv
│── README.md
```

---

## Installation

Install the required libraries:

```bash id="fqgcb4"
pip install requests beautifulsoup4
```

---

## Run the Project

Run the scraper using:

```bash id="iyc1so"
python quotes_scrape.py
```

After execution, a file named:

```text id="eyxhgj"
quotes.csv
```

will be created automatically.

---

## Output

The CSV file contains:

* Quote Text
* Author Name
* Author Link
* Tags

---

## Concepts Used

* Web Scraping
* HTML Parsing
* Pagination
* CSV File Handling

---

## Author

Agi
