from django import forms
from sliders.models import Slider1, Slider2,Slider3
from utils import utils

class Slider1Form(forms.ModelForm):
    class Meta:
        model = Slider1
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        return utils.allowed_one(Slider1, self.instance.pk, cleaned_data)

class Slider2Form(forms.ModelForm):
    class Meta:
        model = Slider1
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        return utils.allowed_one(Slider2, self.instance.pk, cleaned_data)

class Slider3Form(forms.ModelForm):
    class Meta:
        model = Slider1
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        return utils.allowed_one(Slider3, self.instance.pk, cleaned_data)