from django import forms
from .models import Phonenumber, MobileNumber,SchoolTiming, LogoImage

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = Phonenumber
        fields = ['phone_number']

    def clean(self):
        cleaned_data = super().clean()
        if Phonenumber.objects.count() >= 1 and not self.instance.pk:
            raise forms.ValidationError("Only one phone number is allowed.")
        return cleaned_data

class MobileNumberForm(forms.ModelForm):
    class Meta:
        model = MobileNumber
        fields = ['mobile_number']

    def clean(self):
        cleaned_data = super().clean()
        if MobileNumber.objects.count() >= 1 and not self.instance.pk:
            raise forms.ValidationError("Only one mobile number is allowed.")
        return cleaned_data


class SchoolTimingForm(forms.ModelForm):
    start_time = forms.TimeField(
        widget=forms.TimeInput(format='%I:%M %p'),  
        input_formats=['%I:%M %p', '%H:%M']
    )
    end_time = forms.TimeField(
        widget=forms.TimeInput(format='%I:%M %p'),  
        input_formats=['%I:%M %p', '%H:%M']
    )

    class Meta:
        model = SchoolTiming
        fields = ['start_time', 'end_time']

    def clean(self):
        cleaned_data = super().clean()
        if SchoolTiming.objects.count() >= 1 and not self.instance.pk:
            raise forms.ValidationError("Only one time allowed to create school time.")
        return cleaned_data


class LogoImageForm(forms.ModelForm):
    class Meta:
        model = LogoImage
        fields = ['logo']

    def clean(self):
        cleaned_data = super().clean()
        if LogoImage.objects.count() >= 1 and not self.instance.pk:
            raise forms.ValidationError("Only one time allowed to create school time.")
        return cleaned_data