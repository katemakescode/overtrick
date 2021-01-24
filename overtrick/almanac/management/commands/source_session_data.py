from django.core.management.base import BaseCommand

from ._scrape_sessions import scrape


class Command(BaseCommand):
    help = 'Scrapes sessions data for the specified club'

    def add_arguments(self, parser):
        parser.add_argument('club_id', type=int)

    def handle(self, *args, **options):
        scrape(options["club_id"])
