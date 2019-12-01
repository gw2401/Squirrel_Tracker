from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel

from django.views.generic.edit import UpdateView

def all_squirrel_sightings(request):
    if request.method == 'GET':
        squirrels = Squirrel.objects.all()
        context = {
           'squirrels':squirrels,
            }
        return render(request,'apple/all.html',context)

class update(UpdateView):
    if request.method == 'POST':
        squirrels = Squirrel.objects.all()
        context {
                'squirrels': squirrels }
        return render(request,'apple/squirrel_uodate_form.html',context) 
    #template_name_suffix = '_update_form'

#def update(UpdateView)i:
#    if request.method == 'POST':
#    	model = Squirrel
#    	fields = ['Unique_Squirrel_ID']
#    	template_name_suffix = '_update_form'
        
#        return render(request,'apple/squirrel_update_form.html',context)
## Create your views here.
