from django.contrib import admin
from .models import AboutModel

@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url')
    search_fields = ('title',)
    list_filter = ('title',)