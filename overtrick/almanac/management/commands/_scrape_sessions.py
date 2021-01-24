import csv

import requests
from bs4 import BeautifulSoup


def scrape(club_id):
    url = f'https://pairs.bridgenz.co.nz/?club={club_id}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    sessions = soup.select('.score_table_row')

    with open('session.csv', mode='w') as file:
        writer = csv.writer(file)

        for session in sessions:
            data = session.find_all('td')
            values = [x.text for x in data[0:4]]
            writer.writerow(values)
