# Veterinary Companies Web Scraping

A collection of Python web scraping scripts designed to extract company information from multiple veterinary industry websites. Each scraper targets a different website and exports the extracted data into CSV format for further analysis.

## Project Overview

This project contains **five independent web scraping scripts**, each designed to collect company information from a specific veterinary-related website.

The extracted information may include:

- Company Name
- Company ID
- Category
- Country
- Email Address
- Phone Number
- Website

---

## Scraped Websites

| Website | Technique | Extracted Data |
|----------|-----------|----------------|
| London Vet Show | BeautifulSoup | Company Names |
| Richard Wolf | BeautifulSoup | Company Contact Information |
| BSAVA Congress | Selenium + BeautifulSoup | Company Contact Information |
| DNA Vet Care | BeautifulSoup | Company Contact Information |
| VMX (NAVC Exhibitor List) | Selenium | Company Name, Phone Number, Website |

---

## Project Structure

```
Veterinary-Web-Scraping/
│
├── London Vet Scrapping.py
├── Richard Wolf Scrapping.py
├── Bsava Scrapping Using Selenium.py
├── DNA Vet Scrapping.py
├── VMX.py
│
├── London Vet.csv
├── Richard Wolf.csv
├── BSAVA.csv
├── DNA Vet.csv
└── VMX.csv
```

---

## Technologies Used

- Python 3
- BeautifulSoup4
- Selenium
- urllib
- Regular Expressions (re)
- CSV

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YourUsername/Veterinary-Web-Scraping.git
```

Install the required packages:

```bash
pip install beautifulsoup4 selenium
```

If you're using the Selenium-based scrapers, make sure you have **Google Chrome** installed along with the appropriate **ChromeDriver** version.

---

## Running the Scripts

Each scraper can be executed independently.

Example:

```bash
python "London Vet Scrapping.py"
```

or

```bash
python "VMX.py"
```

Each script generates its own CSV file containing the extracted data.

---

## Output Example

| ID | Company Name | Category | Country | Email | Phone | Website |
|----|--------------|----------|---------|-------|-------|---------|
| 1 | ABC Company | Equipment | USA | info@abc.com | +1-555-1234 | https://abc.com |

---

## Features

- Scrapes data from multiple veterinary industry websites.
- Supports both static and dynamic websites.
- Uses **BeautifulSoup** for HTML parsing.
- Uses **Selenium** for JavaScript-rendered pages.
- Automatically exports extracted data to CSV files.
- Easy to extend by adding new website scrapers.

---

## Notes

- Some websites require Selenium because their content is dynamically loaded.
- Website layouts may change over time, requiring updates to the scraping logic.
- Please respect each website's Terms of Service and robots.txt before scraping.
- This project is intended for educational and research purposes only.

---

## Author

**Mohamed Saber**

Data Engineer | Python | Web Scraping | SQL | Power BI
