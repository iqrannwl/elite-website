from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

ICON_CHOICES = [
    ('fa-facebook', 'Facebook'),
    ('fa-twitter', 'Twitter'),
    ('fa-linkedin', 'LinkedIn'),
    ('fa-instagram', 'Instagram'),
    ('fa-youtube', 'YouTube'),
]

class SocialLink(models.Model):
    url = models.URLField()
    icon_class = models.CharField(max_length=50, choices=ICON_CHOICES)

    def __str__(self):
        return self.get_icon_class_display()


class Phonenumber(models.Model):
    phone_number = PhoneNumberField(region="PK")

class MobileNumber(models.Model):
    mobile_number = PhoneNumberField(region="PK")


class SchoolTiming(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()


class WeeklyschoolTiming(models.Model):
    day = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day} - {self.start_time} to {self.end_time}"

class LogoImage(models.Model):
    logo = models.ImageField(upload_to='logos/')