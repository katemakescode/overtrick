import requests
from bs4 import BeautifulSoup

def scrape(club_id):
    print(f'Scraping session data for club {club_id}')
    url = f'https://pairs.bridgenz.co.nz/?club={club_id}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.h2.text)
