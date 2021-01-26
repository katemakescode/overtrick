from pathlib import Path

import requests
from bs4 import BeautifulSoup

from django.conf import settings
from pairs.models import Pair


PAIR_FIELDS = ['number', 'place', 'players', 'points']


def scrape(club_id, date, time):
    filename = f'overtrick/data/{club_id}-{date}{time}.html'
    with open(settings.BASE_DIR / filename) as f:
        soup = BeautifulSoup(f, 'html.parser')

    pairs = soup.select('.score_table_row')
    for pair in pairs:
        data = {
            field_name: pair.find_all('td')[i].text
            for i, field_name in enumerate(PAIR_FIELDS)
        }
        values = {'number': data['number']}
        values['points'] = data['points'].split('/')[0]
        values['player_a'], values['player_b'] = data['players'].split('/')

        p = Pair(**values)
        p.save()
