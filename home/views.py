from django.shortcuts import render
from sliders.models import Slider2, Slider1, Slider3
from about.models import AboutModel
from utils import utils

def home_page(request):
    slider1 = Slider1.objects.all()
    slider2 = Slider2.objects.all()
    slider3 = Slider3.objects.all()

    #about
    about = AboutModel.objects.all()


    return render(request, 'home.html', {
        "slider1": slider1,
        "slider2": slider2,
        "slider3": slider3,
        "about": about,
        **utils.get_context()
    })