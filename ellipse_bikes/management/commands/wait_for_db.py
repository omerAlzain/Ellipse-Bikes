import time

from django.core.management import BaseCommand


class Command(BaseCommand):
    """Wait for the database to be available."""
    def handle(self, *args, **kwargs):
        from django.db import connection
        while True:
            try:
                # None means everything is okay, otherwise it will throw an error if something wrong
                if not connection.ensure_connection():
                    break
            except Exception as e:
                self.stdout.write(self.style.SUCCESS("Deadly waiting for database ..." + str(e)))
                time.sleep(1)
        print('Database is available!')
