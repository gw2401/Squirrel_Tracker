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

def squirrel_update(request, unique_squirrel_id):
    template = 'apple/form.html'
    squirrel = get_object_or_404(Squirrel,Unique_Squirrel_ID=unique_squirrel_id)
    form = SquirrelForm(request.POST or None, instance=squirrel)
    if form.is_valid():
        form.save()
        return redirect('apple:all_squirrel_sightings')
    context = {"form": form}
    return render(request, template, context)      

def squirrel_delete(request, unique_squirrel_id):
    template = 'apple/delete.html'
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=unique_squirrel_id)
    if request.method == 'POST':
        squirrel.delete()
        return redirect('apple:all_squirrel_sightings')
    context = {"squirrel": squirrel}
    return render(request, template, context)

def squirrel_create(request):
    template = 'apple/form.html'
    form = SquirrelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('apple:all_squirrel_sightings')
    context = {"form": form}
    return render(request, template, context)

def squirrel_stats(request):
    template = 'apple/stats.html' 
    from django.db.models import Count
    if request.method == 'GET':
        running_true_frequency = Squirrel.objects.values('Running').annotate(Count(True)).order_by()
        running_false_frequency = Squirrel.objects.values('Running').annotate(Count(False)).order_by() 
    
        context = {
           'true_frequency':true_frequency,
           'false_frequency':false_frequency, 
            }
        return render(request,'apple/all.html',context)
