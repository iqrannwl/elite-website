from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class CompulsorySubjects(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subject_name}"
class ElactiveSubjects(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subject_name}"

class CoursePage(models.Model):
    image = models.ImageField(upload_to="course_images/", null=True, blank=True)
    course_name = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    course_detail = RichTextUploadingField()
    duration = models.CharField(max_length=255)
    elective_subjects = models.ManyToManyField(ElactiveSubjects, related_name="course_elective_subjects", null=True, blank=True)
    compulsory_subjects = models.ManyToManyField(CompulsorySubjects, related_name="course_compulsory_subjects", null=True, blank=True)
