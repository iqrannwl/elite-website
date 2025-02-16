from django.contrib import admin
from courses.models import ElactiveSubjects, CompulsorySubjects, CoursePage

@admin.register(CoursePage)
class CoursePageAdmin(admin.ModelAdmin):
    list_display = ('course_name', "duration")

@admin.register(ElactiveSubjects)
class ElactiveSubjectsAdmin(admin.ModelAdmin):
    list_display = ('subject_name', )

@admin.register(CompulsorySubjects)
class CompulsorySubjectsAdmin(admin.ModelAdmin):
    list_display = ('subject_name',)