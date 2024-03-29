from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Squirrel

from django.views.generic.edit import UpdateView
from .forms import SquirrelForm

def all_squirrel_sightings(request):
    if request.method == 'GET':
        squirrel = Squirrel.objects.all()
        context = {
           'squirrel':squirrel,
            }
        return render(request,'apple/all.html',context)

#def squirrel_update(request, Unique_Squirrel_ID):
 #   template = 'apple/edit.html'
  #  squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
   # squirrel = get_object_or_404(Squirrel,Unique_Squirrel_ID=Unique_Squirrel_ID)
   # form = SquirrelForm(request.POST, instance=squirrel)
    #if form.is_valid():
     #   form.save()
      #  return redirect('apple:all_squirrel_sightings')
   # context = {"form": form}
   # return render(request, template, context)      

def squirrel_update(request, Unique_Squirrel_ID):
    template = 'apple/form.html'
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID = Unique_Squirrel_ID) 
  #  form = SquirrelForm(request.POST or request.GET)

    if request.method == "POST": 
        form= SquirrelForm(request.POST, instance = squirrel) 
        if form.is_valid(): 
            form.save() 
            return redirect('apple:all_squirrel_sightings')
    else: 
        form = SquirrelForm(instance= squirrel) 
    
    context ={  
            'form':form, 
            } 
    return render(request,template,context) 

def squirrel_create(request):
    template = 'apple/form.html'
    form = SquirrelForm(request.POST or request.GET)
    if form.is_valid():
        form.save()
        return redirect('apple:all_squirrel_sightings')
    context = {"form": form}
    return render(request, template, context)

#def squirrel_create(request):
 #   template = 'apple/form.html'
  #  if request.method == "POST":
   #     form = SquirrelForm(request.POST)
    #    if form.is_valid():
     #       form.save()
      #      return redirect('apple:all_squirrel_sightings')
    
   # context = {
    #        "form": form,
     #       }
   # return render(request, template, context)

def squirrel_stats(request):
    from django.db.models import Count
    if request.method == 'GET':
        running_t_frequency = Squirrel.objects.values("Running").order_by('Running').annotate(running_t_frequency = Count("Running"))
        chasing_t_frequency = Squirrel.objects.values("Chasing").order_by('Chasing').annotate(chasing_t_frequency = Count("Chasing"))
        climbing_t_frequency = Squirrel.objects.values("Climbing").annotate(climbing_t_frequency = Count("Climbing")).order_by()
        eating_t_frequency = Squirrel.objects.values("Eating").annotate(eating_t_frequency = Count("Eating")).order_by()
        foraging_t_frequency = Squirrel.objects.values("Foraging").annotate(foraging_t_frequency = Count("Foraging")).order_by()

        context = {
            'running_t_frequency': running_t_frequency,
            'chasing_t_frequency': chasing_t_frequency,
            'climbing_t_frequency': climbing_t_frequency,       
            'eating_t_frequency': eating_t_frequency,
            'foraging_t_frequency': foraging_t_frequency,
            }
        return render(request,'apple/stats.html',context)

def map(request):
    if request.method == 'GET':
        squirrels = Squirrel.objects.all()[:100]
       # latitude = Squirrel.objects.values("Latitude")
       # Longtitude = Squirrel.objects.values("Longtitude")
        context = {
                'squirrels': squirrels,
                }
        return render(request,'apple/map.html',context)





