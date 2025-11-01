"""A Web scrape program to find the number of upcoming events from the Commevents Hub website."""

import requests
from bs4 import BeautifulSoup

url = "https://commeventshub.onrender.com/" # Website URL
response = requests.get(url) # Initiating HTTP GET requests to website URL.
soup = BeautifulSoup(response.text, 'html.parser')

"""Find the number of upcoming events"""
event_count = soup.find('span', class_='badge bg-primary').text
print(f"The number of upcoming events are : {event_count}")