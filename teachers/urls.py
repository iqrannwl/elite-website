from django.urls import path
from .views import teachers_page

urlpatterns = [
    path('', teachers_page, name='teachers'),
]