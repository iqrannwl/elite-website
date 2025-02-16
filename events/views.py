from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.

def events_page(request):
    return render(request, 'events.html')