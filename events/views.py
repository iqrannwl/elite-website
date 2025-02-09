from django.shortcuts import render
from django.views.generic import ListView
from events.models import Event


# Create your views here.

def events_page(request):
    events=Event.objects.all()
    return render(request, 'events.html', {"events":events})

def event_detail(request,id):
    event=Event.objects.get(id=id)
    return render(request, 'event_detail.html', {"event":event})