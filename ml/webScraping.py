import pandas as pd
from bs4 import BeautifulSoup

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.ambitionbox.com/',
    'DNT': '1',
}

session = requests.Session()
session.headers.update(headers)

url = 'https://www.ambitionbox.com/list-of-companies?page=1'
response = session.get(url)

print("Status Code:", response.status_code)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    companyDetails = soup.find_all('div', class_='companyCardWrapper')

    companies = []
    ratings = []
    domains = []
    reviews = []
    salaries = []
    interviews = []
    jobs = []
    benefits = []
    photos = []

    for cmpny in companyDetails:
        name = cmpny.find('h2', class_='companyCardWrapper__companyName').text.strip()
        rating = cmpny.find('div', class_='rating_text').text.strip()
        domain = cmpny.find('span', class_='companyCardWrapper__interLinking').text.split('|')[0].strip()
        companies.append(name)
        ratings.append(rating)
        domains.append(domain)

        actions = cmpny.find_all('a', class_='companyCardWrapper__ActionWrapper')
        for ac in actions:
            title = ac.find('span', class_='companyCardWrapper__ActionTitle').text.strip()
            count = ac.find('span', class_='companyCardWrapper__ActionCount').text.strip()
            if 'review' in title.lower():
                reviews.append(count)
            if 'salaries' in title.lower():
                salaries.append(count)
            if 'interview' in title.lower():
                interviews.append(count)
            if 'job' in title.lower():
                jobs.append(count)
            if 'benefit' in title.lower():
                benefits.append(count)
            if 'photo' in title.lower():
                photos.append(count)

    jobs = [None if '--' in jb else jb for jb in jobs]
    data = {
        "companies": companies,
        "ratings": ratings,
        "domains": domains,
        "reviews": reviews,
        "salaries": salaries,
        "interviews": interviews,
        "jobs": jobs,
        "benefits": benefits,
        "photos": photos
    }

    df = pd.DataFrame(data)
    print("data :: ", data)

else:
    print("Failed. Content:", response.text[:500])
