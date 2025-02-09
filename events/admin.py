from django.contrib import admin
from events.models import Event

@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    list_display=["id", "title", "date"]