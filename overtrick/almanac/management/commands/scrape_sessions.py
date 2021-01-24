from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Scrapes sessions data for the specified club'

    def add_arguments(self, parser):
        parser.add_argument('club_id', type=int)

    def handle(self, *args, **options):
        self.scrape(options["club_id"])

    def scrape(self, club_id):
        print(f'hello {club_id}')
