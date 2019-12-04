
from django.core.management.base import BaseCommand, CommandError
import datetime, csv
from apple.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        fields = [i.name for i in Squirrel._meta.fields]

        with open(path, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(fields)
            for obj in Squirrel.objects.all():
                writer.writerow([getattr(obj, f) for f in fields])
