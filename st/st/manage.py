#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#def try():
#    print ('hello')

#def import_squirrel_data(path):
#     import csv
#     from apple.models import Squirrel
#     with open(path, 'rt') as f:
#        reader = csv.reader(f, dialect='excel')
#        for row in reader:
#             squirrel = Squirrel.objects.create(
#                            Latitude = row[0],
#                            Longitude = row[1],
#                            Unique_Squirrel_ID = row[2],
#                            Shift = row[4],
#                            Date = row[5],
#                            Age = row[7],
#                            Primary_Fur_Color = row[8],
#                            Location = row[12],
#                            Specific_Location = row[14],
#                            Running = row[15],
#                            Chasing = row[16],
#                            Climbing = row[17],
#                            Eating = row[18],
#                            Foraging = row[19],
#                            Other_Activities = row[20],
#                            Kuks = row[21],
#                            Quaas = row[22],
#                            Moans = row[23],
#                            Tail_flags = row[24],
#                            Tail_twitches = row[25],
#                            Approaches = row[26],
#                            Indifferent = row[28],
#                            Runs_from = row[28],
#                            ) 

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'st.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
