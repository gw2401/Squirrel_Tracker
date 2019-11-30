import os
import csv

from django.core.management.base import BaseCommand, CommandError
from datetime import datetime

class Command(BaseCommand):
     help = "Import students by homeroom."

     def add_arguments(self, parser):
         parser.add_argument('path')

     def handle(self,path,**options):
         import csv
         from apple.models import Squirrel
         to_bool = lambda x: True if x == 'TRUE' else False
#         import os
#	     THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
#             my_file = os.path.join(THIS_FOLDER, 'myfile.txt')
#	 path = str(path)
         with open(path, 'r') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                 squirrel = Squirrel.objects.get_or_create(
                            Latitude = float(row[0]),
                            Longitude = float(row[1]),
                            Unique_Squirrel_ID = row[2],
                            Shift = row[4],
                            Date = datetime.strptime(row[5],'%m%d%Y'),
                            Age = row[7],
                            Primary_Fur_Color = row[8],
                            Location = row[12],
                            Specific_Location = row[14],
                            Running = to_bool(row[15]),
                            Chasing = to_bool(row[16]),
                            Climbing = to_bool(row[17]),
                            Eating = to_bool(row[18]),
                            Foraging = to_bool(row[19]),
                            Other_Activities = to_bool(row[20]),
                            Kuks = to_bool(row[21]),
                            Quaas = to_bool(row[22]),
                            Moans = to_bool(row[23]),
                            Tail_flags = to_bool(row[24]),
                            Tail_twitches = to_bool(row[25]),
                            Approaches = to_bool(row[26]),
                            Indifferent = to_bool(row[28]),
                            Runs_from = to_bool(row[28]),
                            )

