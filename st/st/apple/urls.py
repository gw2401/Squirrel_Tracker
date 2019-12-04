from django.urls import path,re_path

from . import views

app_name = 'apple'



urlpatterns = [
        path('sightings/',views.all_squirrel_sightings,name = 'all_squirrel_sightings'),
        re_path(r'sightings/(?P<unique_squirrel_id>\w+\-\w+\-\d{4}\-\d{2})/', views.squirrel_update,name = 'update'),

        re_path(r'sightings/(?P<unique_squirrel_id>\w+\-\w+\-\d{4}\-\d{2})/delete', views.squirrel_delete, name = 'delete'),
        path('sightings/add/', views.squirrel_create, name='add'),
        path('sightings/stats/', views.squirrel_stats, name='stats'),

        ]
