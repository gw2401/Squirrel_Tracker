import os
import csv

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
     help = "Import students by homeroom."

     def add_arguments(self, parser):
         parser.add_argument('path')

     def handle(self,path,**options):
         import csv
         from apple.models import Squirrel
#         import os
#	     THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
#             my_file = os.path.join(THIS_FOLDER, 'myfile.txt')
#	 path = str(path)
         with open(path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                 squirrel = Squirrel.objects.get_or_create(
                            Latitude = row[0],
                            Longitude = row[1],
                            Unique_Squirrel_ID = row[2],
                            Shift = row[4],
                            Date = row[5],
                            Age = row[7],
                            Primary_Fur_Color = row[8],
                            Location = row[12],
                            Specific_Location = row[14],
                            Running = row[15],
                            Chasing = row[16],
                            Climbing = row[17],
                            Eating = row[18],
                            Foraging = row[19],
                            Other_Activities = row[20],
                            Kuks = row[21],
                            Quaas = row[22],
                            Moans = row[23],
                            Tail_flags = row[24],
                            Tail_twitches = row[25],
                            Approaches = row[26],
                            Indifferent = row[28],
                            Runs_from = row[28],
                            )

