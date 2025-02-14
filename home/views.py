from django.shortcuts import render
from home.models import SocialLink, MobileNumber, Phonenumber, SchoolTiming
# Create your views here.
def home_page(request):
    social_links = SocialLink.objects.all()
    mobile_numbers = MobileNumber.objects.get(id=1)
    phone_numbers = Phonenumber.objects.get(id=1)
    school_timings = SchoolTiming.objects.get(id=1)
    return render(request, 'home.html', {
        "social_links": social_links,
        "mobile_numbers": mobile_numbers,
        "phone_number": phone_numbers,
        "school_timing": school_timings,
        })