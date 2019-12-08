import os
import csv

from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from distutils.util import strtobool

class Command(BaseCommand):

     def add_arguments(self, parser):
         parser.add_argument('path')

     def handle(self,path,**options):
         import csv
         from apple.models import Squirrel
         with open(path, 'r') as f:
             reader = csv.reader(f)
             next(reader, None)
             for row in reader: 
                 squirrel = Squirrel(
                            Latitude = float(row[0]),
                            Longitude = float(row[1]),
                            Unique_Squirrel_ID = row[2],
                            Shift = row[4],
                            Date = datetime.strptime(row[5],'%m%d%Y'),
                            Age = row[7],
                            Primary_Fur_Color = row[8],
                            Location = row[12],
                            Specific_Location = row[14],
                            Running = strtobool(row[15]),
                            Chasing = strtobool(row[16]),
                            Climbing = strtobool(row[17]),
                            Eating = strtobool(row[18]),
                            Foraging = strtobool(row[19]),
                            Other_Activities = row[20],
                            Kuks = strtobool(row[21]),
                            Quaas = strtobool(row[22]),
                            Moans = strtobool(row[23]),
                            Tail_flags = strtobool(row[24]),
                            Tail_twitches = strtobool(row[25]),
                            Approaches = strtobool(row[26]),
                            Indifferent = strtobool(row[28]),
                            Runs_from = strtobool(row[28]),
                            )
                 squirrel.save()
            
            

