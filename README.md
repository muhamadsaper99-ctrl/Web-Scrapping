#  Veterinary Companies Web Scraping

A collection of Python web scraping scripts designed to extract company information from different veterinary-related websites.

##  Project Overview

This project contains four independent web scraping scripts. Each script targets a different website and exports the extracted data into a CSV file.

The collected information may include:

- Company Name
- Country
- Email Address
- Phone Number
- Website
- Company ID

---

##  Scraped Websites

| Website | Technique | Output |
|----------|-----------|--------|
| London Vet Show | BeautifulSoup | Company Names |
| Richard Wolf | BeautifulSoup | Company Contact Information |
| BSAVA Congress | Selenium + BeautifulSoup | Company Contact Information |
| DNA Vet Care | BeautifulSoup | Company Contact Information |

---

##  Technologies Used

- Python 3
- BeautifulSoup4
- Selenium
- urllib
- CSV

---

##  Installation

Clone the repository

```bash
git clone https://github.com/YourUsername/Veterinary-Web-Scraping.git
```

Install dependencies

```bash
pip install beautifulsoup4 selenium
```

Download the appropriate ChromeDriver compatible with your Chrome version if you want to run the Selenium scraper.

---

##  Running the Scripts

Run any scraper individually.

Example:

```bash
python "London Vet Scrapping.py"
```

or

```bash
python "Bsava Scrapping Using Selenium.py"
```

Each script generates its own CSV file.

---

##  Output Example

| ID | Company Name | Country | Email | Phone | Website |
|----|--------------|---------|-------|-------|---------|
| 1 | ABC Company | UK | info@abc.com | +44xxxx | abc.com |

---

##  Notes

- Some websites require Selenium because their content is dynamically loaded.
- Website structures may change over time, which can require updating the scraping logic.
- These scripts are intended for educational and research purposes only.

---

## Author

**Mohamed Saber**
