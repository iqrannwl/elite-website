from django.shortcuts import render

# Create your views here.

def courses_page(request):
    return render(request, 'courses.html')