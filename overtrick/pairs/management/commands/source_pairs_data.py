from django.core.management.base import BaseCommand

from ._scrape_pairs import scrape


class Command(BaseCommand):
    help = 'Scrapes pairs data for the specified session'

    def add_arguments(self, parser):
        parser.add_argument('session_id', type=int)

    def handle(self, *args, **options):
        scrape(options["session_id"])
