from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Teacher(models.Model):
    image = models.ImageField(upload_to="teachers/")
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, null=True, blank=True)
    qualification = models.CharField(max_length=255, null=True, blank=True)
    description = RichTextUploadingField()

