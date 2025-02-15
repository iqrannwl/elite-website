from django.contrib import admin
from sliders.models import Slider3, Slider1, Slider2
from sliders.forms import Slider1Form, Slider2Form, Slider3Form


@admin.register(Slider1)
class Slider1Admin(admin.ModelAdmin):
    form = Slider1Form
    list_display = ["id", "heading", "image"]

@admin.register(Slider2)
class Slider2Admin(admin.ModelAdmin):
    form = Slider2Form
    list_display = ["id", "heading", "image"]

@admin.register(Slider3)
class Slider3Admin(admin.ModelAdmin):
    form = Slider3Form
    list_display = ["id", "heading", "image"]