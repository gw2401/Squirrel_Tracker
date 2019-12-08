from django.db import models

class Squirrel(models.Model):
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Unique_Squirrel_ID = models.CharField(max_length=20)
    
    AM = 'AM' 
    PM = 'PM' 
    SHIFT_CHOICES = ( 
          (AM, 'AM'), 
          (PM, 'PM'), 
           ) 
    Shift = models.CharField( 
    max_length=5, 
    choices=SHIFT_CHOICES, 
    default=AM,
    ) 

    Date = models.DateField()

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    AGE_CHOICES =  ( (ADULT, 'Adult'),
             (JUVENILE, 'Juvenile'),
             )

    Age = models.CharField( 
     max_length=10, 
     choices=AGE_CHOICES, 
     blank = True, 
     ) 

    GRAY = 'Gray' 
    CINNAMON = 'Cinnamon' 
    BLACK = 'Black' 
    COLOR_CHOICES = ( 
     (GRAY, 'Gray'), 
     (CINNAMON, 'Cinnamon'), 
     (BLACK, 'Black'),
     ) 
    
    Primary_Fur_Color = models.CharField( 
     max_length=10, 
     choices=COLOR_CHOICES, 
     blank = True, 
     ) 


    GP = 'Ground Plane'
    AG = 'Above Ground'
    LOCATION_CHOICES = (
     (GP, 'Ground Plane'),
     (AG, 'Above Ground'),
     )
     
    Location = models.CharField(
     max_length=20,
     choices=LOCATION_CHOICES,
     blank = True,
     )
  
    Specific_Location = models.CharField(max_length = 100)
    
    Running = models.BooleanField(default = True)

    Chasing = models.BooleanField(default = True)

    Climbing = models.BooleanField(default = True)

    Eating = models.BooleanField(default = True)

    Foraging = models.BooleanField(default = True)

    Other_Activities = models.CharField(max_length = 100)

    Kuks = models.BooleanField(default = True)

    Quaas = models.BooleanField(default = True)

    Moans = models.BooleanField(default = True)

    Tail_flags =models.BooleanField(default = True)

    Tail_twitches =models.BooleanField(default = True)

    Approaches = models.BooleanField(default = True)

    Indifferent =models.BooleanField(default = True)

    Runs_from = models.BooleanField(default = True)  # Create your models here.
