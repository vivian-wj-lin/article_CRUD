from django.db import connections
from django.core.management.base import BaseCommand

import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                connections['default'].cursor()
                db_up = True
            except Exception:
                self.stdout.write("Database unavailable, please wait...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available."))
