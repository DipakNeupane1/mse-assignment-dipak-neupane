"""A Web scrape program to find the number of upcoming events from the Commevents Hub website."""

import requests
from bs4 import BeautifulSoup

url = "https://commeventshub.onrender.com/" # Website URL
response = requests.get(url) # Initiating HTTP GET requests to website URL.
soup = BeautifulSoup(response.text, 'html.parser')

"""Find the number of upcoming events"""
event_count = soup.find('span', class_='badge bg-primary').text
print(f"The number of upcoming events are : {event_count}")

# Retrieve event counts as per category with each links
categories = {
    "Māori": "/events/tag/m%C4%81ori",
    "Pacific": "/events/tag/pacific",
    "General": "/events/tag/general",
}

for category, path in categories.items():
    category_url = f"{url}{path}"
    category_response = requests.get(category_url)
    category_soup = BeautifulSoup(category_response.text, 'html.parser')

    # Find all the event cards from each event is within a <div class="card">
    events = category_soup.find_all("div", class_="card")
    event_count = len(events)

    print(f"{category} events: {event_count}")