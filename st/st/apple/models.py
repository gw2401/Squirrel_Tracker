from django.db import models
class Squirrel(models.Model):
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Unique_Squirrel_ID = models.CharField(max_length=15)
    Shift = models.CharField(max_length=2)
    Date = models.DateField()
    Age = models.CharField(max_length = 100)
    Primary_Fur_Color = models.CharField(max_length = 100)
    Location = models.CharField(max_length = 100)
    Specific_Location = models.CharField(max_length = 100)
    Running = models.CharField(max_length = 100)

    Chasing = models.CharField(max_length = 100)

    Climbing = models.CharField(max_length = 100)

    Eating = models.CharField(max_length = 100)

    Foraging = models.CharField(max_length = 100)

    Other_Activities = models.CharField(max_length = 100)
    Kuks = models.CharField(max_length = 100)

    Quaas = models.CharField(max_length = 100)

    Moans = models.CharField(max_length = 100)

    Tail_flags =models.CharField(max_length = 100)

    Tail_twitches =models.CharField(max_length = 100)

    Approaches = models.CharField(max_length = 100)

    Indifferent =models.CharField(max_length = 100)

    Runs_from = models.CharField(max_length = 100)  # Create your models here.
