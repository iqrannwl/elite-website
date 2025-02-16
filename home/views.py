from django.shortcuts import render
from sliders.models import Slider2, Slider1, Slider3
from about.models import AboutModel
from courses.models import CoursePage
from teachers.models import Teacher
from gallery.models import Gallery, ImageType
from utils import utils

def home_page(request):
    slider1 = Slider1.objects.all()
    slider2 = Slider2.objects.all()
    slider3 = Slider3.objects.all()

    #about
    about = AboutModel.objects.all()
    course = CoursePage.objects.all()
    teacher = Teacher.objects.all()
    gallery = Gallery.objects.prefetch_related('image_type')
    image_type = ImageType.objects.all()
    return render(request, 'home.html', {
        "slider1": slider1,
        "slider2": slider2,
        "slider3": slider3,
        "about": about,
        "courses": course,
        "teachers": teacher,
        "image_types": image_type,
        "gallery_list": gallery,
        **utils.get_context()
    })