from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import StartForm, p1Form, p1_1Form, p1_2Form, p2Form
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, '../templates/home/home.html')

#we start at the start page with this view and redirect users to different urls depending on their input/choices
def start_page(request):
    #used to figure out where to send the user after their input
    #each path has its own url which branches out from there
    paths = {
        'path_1': {'topic':["portraits", "landscapes"], 'url': '/p1'},
        'path_2': {'topic':["friends", "snapshots"],'url': '/p2'},
        'path_3': {'topic':["everything"],'url': '/p3'}
    }
    
    if request.method == 'POST':
        form = StartForm(request.POST)
        if form.is_valid():
            input = form.cleaned_data['input']
            for path in paths:
                if input in paths[path]['topic']:
                    return HttpResponseRedirect(paths[path]['url'])
            messages.add_message(request, messages.INFO, "Didn't quite get that. Please try again")
        
    form = StartForm()
    return render(request, 'startform/startform.html', {'form': form })

#after being redirected down path 1, two branches from here named p1_1 and p1_2
def portrait_landscape_view(request):
    if request.method == 'POST':
        print(request.POST)
        if 'Fixed' in request.POST['btn']:
            return HttpResponseRedirect('/p1/1')
        elif 'Interchangeable' in request.POST['btn']:
            return HttpResponseRedirect('/p1/2')
        
    form=p1Form()
    return render(request, 'paths/p1.html', {'form': form })

#still on path 1, this is p1_1
def portrait_landscape_fixed_lens(request):
    if request.method == 'POST':
        if 'Mechanical' in request.POST['btn']:
            return HttpResponseRedirect('/p1/1/olympus_rc')
        elif 'Battery' in request.POST['btn']:
            return HttpResponseRedirect('/p1/2/olympus_xa')

    form = p1_1Form()
    return render(request, 'paths/p1_1.html', {'form': form })

#this is p1_2
def portrait_landscape_interchangeable_lens(request):
    if request.method == 'POST':
        if 'Mechanical' in request.POST['btn']:
            return HttpResponseRedirect('/p1/1/nikon_fm')
        elif 'Battery' in request.POST['btn']:
            return HttpResponseRedirect('/p1/2/nikon_fe')
    form = p1_2Form()
    return render(request, 'paths/p1_2.html', {'form': form })

#this is where path 2 starts
def friend_or_snapshot_view(request):
    
    if request.method == 'POST':
        form = p2Form(request.POST)
        if form.is_valid():
            budget = int(form.data['budget'])
            if budget <= 50:
                return HttpResponseRedirect('/pentax_iq')
            elif 150 > budget > 50:
                return HttpResponseRedirect('/olympus_stylus')
            elif budget >= 150:
                return HttpResponseRedirect('/konica_bigmini')
        
    form = p2Form()
    return render(request, 'paths/p2.html', {'form': form })

#include model data
def pentax_iq_view(request):
    return render(request, 'cameras/pentax_iq.html')
#include model data
def olympus_stylus_view(request):
    return render(request, 'cameras/olympus_stylus.html')
#include model data
def konica_bigmini_view(request):
    return render(request, 'cameras/konica_bigmini.html')
    

#this view handles path 3, which is straight to a recommendation
def everything_view(request):
    return render(request, 'cameras/minolta_himatic.html')