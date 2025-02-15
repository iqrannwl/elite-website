from django import forms
from headers.models import SocialLink, MobileNumber, Phonenumber, SchoolTiming, LogoImage

def allowed_one(model, instance,cleaned_data,  massage=None):
    if model.objects.count() >= 1 and not instance:
        if massage:
            raise forms.ValidationError(massage)
        raise forms.ValidationError("Not allowed")
    return cleaned_data

def get_context():
    social_links = SocialLink.objects.all()
    mobile_numbers = MobileNumber.objects.get(id=1) if MobileNumber.objects.all().exists() else None
    phone_numbers = Phonenumber.objects.get(id=1) if Phonenumber.objects.all().exists() else None
    school_timings = SchoolTiming.objects.get(id=1) if  SchoolTiming.objects.all().exists() else None
    logo_image = LogoImage.objects.get(id=1) if LogoImage.objects.all() else None
    return {
        "social_links": social_links,
        "mobile_numbers": mobile_numbers,
        "phone_number": phone_numbers,
        "school_timing": school_timings,
        "logo_image": logo_image,
        }