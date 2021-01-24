from urllib.request import urlopen


def scrape(club_id):
    print(f'Scraping session data for club {club_id}')

    html = urlopen(f'https://pairs.bridgenz.co.nz/?club={club_id}')
    print(html.read())
