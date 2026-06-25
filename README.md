# Python Job Listings Scraper

## Project URL

https://roadmap.sh/projects/job-listings-scraper

## Project Overview

This project is a beginner-friendly Python web scraper that collects job listings from the Fake Python Jobs website.

The scraper extracts important job details such as:

- Job Title
- Company Name
- Location
- Job Detail Page URL

The extracted data is saved into a CSV file named `job_listings.csv`.

This project helps beginners understand how web scraping works using Python. It focuses on reading HTML structure, selecting elements, extracting useful data, and storing the results in a structured format.

## Website Used

The data is scraped from:

https://realpython.github.io/fake-jobs/

This website is designed for learning and practicing web scraping, so it is safe and beginner-friendly.

## Technologies Used

- Python 3
- Requests
- BeautifulSoup
- CSV Module

## Features

- Scrapes job listings from the Fake Python Jobs website
- Extracts job title, company name, location, and job detail page URL
- Saves extracted data into a CSV file
- Handles missing fields safely
- Uses clean and readable Python code

## Project Requirements

The scraper should:

- Scrape data from `https://realpython.github.io/fake-jobs/`
- Extract the following fields:
  - Job Title
  - Company Name
  - Location
  - Job Detail Page URL
- Store the results in a CSV file
- Use clean and readable Python code
- Handle simple edge cases such as missing fields

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Nandanarajps/Python-web-scraper.git
