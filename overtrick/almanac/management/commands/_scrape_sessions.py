import requests
from bs4 import BeautifulSoup

from almanac.models import Session

SESSION_FIELDS = ['club', 'date', 'time', 'event']


def scrape(club_id):
    url = f'https://pairs.bridgenz.co.nz/?club={club_id}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    sessions = soup.select('.score_table_row')

    for session in sessions:
        values = {
            field_name: session.find_all('td')[i].text
            for i, field_name in enumerate(SESSION_FIELDS)
        }

        s = Session(**values)
        s.save()
