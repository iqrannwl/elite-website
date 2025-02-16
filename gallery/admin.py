from django.contrib import admin
from gallery.models import Gallery, ImageType

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", 'image')

@admin.register(ImageType)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", 'name')