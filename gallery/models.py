from django.db import models


class ImageType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    image_type = models.ManyToManyField(ImageType)

