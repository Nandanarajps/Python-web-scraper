# Fake Python Jobs Web Scraper

## Project Overview

This project is a beginner-friendly Python web scraper that collects job listings from the Fake Python Jobs website.

The scraper extracts important job details such as:

- Job Title
- Company Name
- Location
- Job Detail Page URL

The extracted data is saved into a CSV file named `job_listings.csv`.

This project is useful for learning the basics of web scraping, HTML parsing, data extraction, and CSV file handling using Python.

---

## Website Used

Source website:

https://realpython.github.io/fake-jobs/

This website is designed for web scraping practice, so it is suitable for beginners.

---

## Technologies Used

- Python 3
- Requests
- BeautifulSoup
- CSV Module

---

## Project Requirements

The scraper should:

- Scrape data from the Fake Python Jobs website.
- Extract job title, company name, location, and job detail page URL.
- Store the extracted data in a CSV file.
- Use clean and readable Python code.
- Handle missing fields safely.

---

## Installation Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fake-python-jobs-scraper.git
```

### 2. Open the project folder

```bash
cd fake-python-jobs-scraper
```

### 3. Install required libraries

```bash
pip install -r requirements.txt
```

---

## How to Run the Project

Run the Python file:

```bash
python job_scraper.py
```

After running the program, a CSV file named `job_listings.csv` will be created in the project folder.

---

## Output File

The output will be stored in:

```text
job_listings.csv
```

The CSV file will contain:

| Job Title | Company Name | Location | Job URL |
|----------|--------------|----------|---------|
| Senior Python Developer | Payne, Roberts and Davis | Stewartbury, AA | Job detail link |
| Energy Engineer | Vasquez-Davidson | Christopherville, AA | Job detail link |

---

## Project Structure

```text
fake-python-jobs-scraper/
│
├── job_scraper.py
├── job_listings.csv
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## Skills Learned

Through this project, you will learn:

- How to send HTTP requests using Python
- How to parse HTML using BeautifulSoup
- How to extract data from HTML elements
- How to handle missing data
- How to save scraped data into a CSV file
- How to create a beginner-friendly Python portfolio project

---

## Future Improvements

Possible improvements:

- Export data to Excel or JSON
- Add search/filter options
- Store data in a database
- Add logging
- Create a simple dashboard using Power BI or Excel
- Automate the scraper using Task Scheduler or cron

---

## License

This project is licensed under the MIT License.

---

## Author

**Nandana**

Computer Science Engineering Student  
Aspiring Data Analyst
