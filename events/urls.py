from django.urls import path
from .views import events_page, event_detail

urlpatterns = [
    path('', events_page, name='events'),
    path("<int:id>", event_detail, name="event_detail")
    
]