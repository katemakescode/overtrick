import requests
from bs4 import BeautifulSoup

from pairs.models import Pair

PAIR_FIELDS = ['club', 'date', 'time', 'event']


def scrape(session_id):
    url = f'https://pairs.bridgenz.co.nz/?club={session_id}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    sessions = soup.select('.score_table_row')

    for session in sessions:
        data = session.find_all('td')
        values = {
            field_name: data[i].text
            for i, field_name in enumerate(PAIR_FIELDS)
        }

        s = Pair(**values)
        s.save()
