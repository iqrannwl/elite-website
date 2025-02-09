from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
    image=models.ImageField(upload_to="blogs/")
    title=models.CharField(max_length=255)
    date=models.DateTimeField()
    description=RichTextUploadingField()