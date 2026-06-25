import requests
from bs4 import BeautifulSoup
import csv


# Website URL
url = "https://realpython.github.io/fake-jobs/"


# Send request to website
response = requests.get(url)


# Check if page loaded successfully
if response.status_code == 200:
    print("Website loaded successfully")
else:
    print("Failed to load website")


# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")


# Find all job cards
jobs = soup.find_all("div", class_="card-content")


# Store jobs data
job_list = []


# Extract information
for job in jobs:

    # Job title
    title = job.find("h2", class_="title")

    if title:
        title = title.text.strip()
    else:
        title = "Not Available"


    # Company name
    company = job.find("h3", class_="company")

    if company:
        company = company.text.strip()
    else:
        company = "Not Available"


    # Location
    location = job.find("p", class_="location")

    if location:
        location = location.text.strip()
    else:
        location = "Not Available"


    # Job detail link
    link = job.find("a")

    if link:
        job_url = link["href"]
    else:
        job_url = "Not Available"


    # Add data
    job_list.append([
        title,
        company,
        location,
        job_url
    ])


# Save data into CSV

with open("job_listings.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Header
    writer.writerow([
        "Job Title",
        "Company Name",
        "Location",
        "Job URL"
    ])

    # Data rows
    writer.writerows(job_list)


print("Scraping completed!")
print("Total jobs collected:", len(job_list))