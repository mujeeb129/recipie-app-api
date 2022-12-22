from django.core.management import BaseCommand
from django.db.utils import OperationalError

import time

from psycopg2.errors import OperationalError as Psycopg2error


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for db to connect...')
        db_up = False
        while db_up == False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2error, OperationalError):
                self.stdout.write('Waiting for a second !')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Connected to Database'))