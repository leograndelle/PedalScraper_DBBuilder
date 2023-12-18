# Guitar Pedal Scraper

## Overview
This script is designed to scrape guitar pedal data from the Andertons website and store it in an SQLite database named 'pedals.db'. The data includes the pedal name, price, star rating, and the number of reviews.

## Dependencies
- **requests:** Used for making HTTP requests to fetch the HTML content of the web pages.
- **BeautifulSoup:** A library for pulling data out of HTML and XML files.
- **sqlite3:** SQLite is used as the database to store the scraped data.
- **time:** Provides functions to add delays in the scraping process.
- **math:** Used for mathematical operations, specifically for calculating the number of pages to scrape.

Make sure to install these dependencies before running the script.

```bash
pip install requests beautifulsoup4
```
## How to Use
1. **Database Connection:** The `connect_db` function establishes a connection to the 'pedals' SQLite database. Ensure that you have the necessary permissions to create and write to a file in the script's directory.

2. **Table Creation:** The `create_table` function creates a table named 'pedals' in the connected database if it doesn't already exist. This table structure includes columns for the pedal name, price, star rating, and the number of reviews.

3. **Scraping Data:** The `scrape_to_db` function scrapes pedal data from multiple pages on the Andertons website and stores it in the 'pedals' table. The scraping is based on the provided URL, and the script takes care of pagination to ensure all available data is collected.

4. **Main Execution:** The script checks if it is being run directly (`__name__ == '__main__'`). If so, it connects to the database, creates the necessary table, specifies the URL for scraping (in this case, EQ pedals from Andertons), and executes the scraping process. Finally, the database connection is closed.

