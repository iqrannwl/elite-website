from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
class AboutModel(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()
    video_url = models.URLField()
    image = models.ImageField(upload_to='about')