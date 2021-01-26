from django.core.management.base import BaseCommand

from ._scrape_pairs import scrape


class Command(BaseCommand):
    help = 'Scrapes pairs data for the specified session'

    def add_arguments(self, parser):
        parser.add_argument('club_id', type=str)
        parser.add_argument('date', type=str)
        parser.add_argument('time', type=str)
        parser.add_argument('event', type=str)

    def handle(self, *args, **options):
        scrape(
            options['club_id'],
            options['date'],
            options['time'],
            options['event'],
        )
