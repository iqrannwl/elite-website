from django.shortcuts import render

# Create your views here.

def teachers_page(request):
    return render(request, 'teachers.html')