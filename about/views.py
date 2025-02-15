from django.shortcuts import render
from about.models import AboutModel
from utils import utils

def about_page(request):
    about = AboutModel.objects.all()
    remove_link = {
        'title': 'About Us',
    }
    return render(request, 'about.html', {'about': about,**remove_link, **utils.get_context()})