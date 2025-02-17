from django.contrib import admin
from headers.models import SocialLink, Phonenumber, MobileNumber, SchoolTiming, LogoImage, WeeklyschoolTiming
from headers.forms import PhoneNumberForm, MobileNumberForm,SchoolTimingForm, LogoImageForm
# Register your models here.

class SchoolTimingAdmin(admin.ModelAdmin):
    form = SchoolTimingForm
    list_display = ("id", "formatted_start_time", "formatted_end_time")

    def formatted_start_time(self, obj):
        return obj.start_time.strftime("%I:%M %p")
    formatted_start_time.short_description = "Start Time"

    def formatted_end_time(self, obj):
        return obj.end_time.strftime("%I:%M %p")
    formatted_end_time.short_description = "End Time"

admin.site.register(SchoolTiming, SchoolTimingAdmin)


@admin.register(LogoImage)
class LogoImageAdmin(admin.ModelAdmin):
    form = LogoImageForm
    list_display = ("id", "logo")


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ["id", "url", "icon_class"]

class PhoneNumberAdmin(admin.ModelAdmin):
    form = PhoneNumberForm
    list_display = ["id","phone_number"]

class MobileNumberAdmin(admin.ModelAdmin):
    form = MobileNumberForm
    list_display = ["id", "mobile_number"]

    def save_model(self, request, obj, form, change):
        return super().save_model(request, obj, form, change)


admin.site.register(Phonenumber, PhoneNumberAdmin)
admin.site.register(MobileNumber, MobileNumberAdmin)

admin.site.register(WeeklyschoolTiming)