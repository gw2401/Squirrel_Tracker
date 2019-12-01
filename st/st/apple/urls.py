from django.urls import path

from . import views

urlpatterns = [
        path('sightings/',views.all_squirrel_sightings),
        path('sightings/<squirrels>',views.update.as_view()),
        ]
