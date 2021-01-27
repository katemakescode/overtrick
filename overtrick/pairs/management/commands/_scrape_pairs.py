from bs4 import BeautifulSoup

from django.conf import settings
from pairs.models import Pair
from almanac.models import Session


PAIR_FIELDS = ['number', 'place', 'players', 'points']


def scrape(club_id, date, time, event):
    filename = f'overtrick/data/{club_id}_{date}_{time}_{event}.html'
    with open(settings.BASE_DIR / filename) as f:
        soup = BeautifulSoup(f, 'html.parser')

    event = event.replace('-', ' ')
    s = Session.objects.get(date=date, time=time, event=event)

    orientations = soup.select('table')[1:3]
    for orientation in orientations:
        label = orientation.select('tr.headings')[0].text
        label = ''.join([direction[0] for direction in label.split('/')])

        pairs = orientation.select('.score_table_row')
        for pair in pairs:
            data = {
                field_name: pair.find_all('td')[i].text
                for i, field_name in enumerate(PAIR_FIELDS)
            }
            values = {
                'session': s,
                'orientation': label,
                'number': data['number'],
                'points': data['points'].split('/')[0]
            }
            values['player_a'], values['player_b'] = data['players'].split('/')

            p = Pair(**values)
            p.save()
