from django.db import models

class Slider1(models.Model):
    heading = models.CharField(max_length=100)
    sub_heading = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='slider1/')
    image2 = models.ImageField(upload_to='image2/', null=True, blank=True)
    show = models.BooleanField(default=True)

class Slider2(models.Model):
    heading = models.CharField(max_length=100)
    sub_heading = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='slider2/')
    image2 = models.ImageField(upload_to='image2/', null=True, blank=True)
    show = models.BooleanField(default=True)

class Slider3(models.Model):
    heading = models.CharField(max_length=100)
    sub_heading = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='slider3/')
    image2 = models.ImageField(upload_to='image2/', null=True, blank=True)
    show = models.BooleanField(default=True)
