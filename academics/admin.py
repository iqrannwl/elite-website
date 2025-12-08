from django.contrib import admin
from .models import (
    Class, Section, Subject, ClassSubject, Timetable,
    Attendance, Examination, ExamSchedule, Grade,
    Homework, HomeworkSubmission
)


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'numeric_value', 'campus', 'class_teacher', 'is_active')
    list_filter = ('campus', 'is_active')
    search_fields = ('name',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_name', 'capacity', 'current_strength', 'room_number', 'is_active')
    list_filter = ('class_name', 'is_active')
    search_fields = ('name', 'room_number')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'subject_type', 'is_elective', 'is_active')
    list_filter = ('subject_type', 'is_elective', 'is_active')
    search_fields = ('name', 'code')


@admin.register(ClassSubject)
class ClassSubjectAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'subject', 'teacher', 'academic_year', 'theory_marks', 'practical_marks')
    list_filter = ('class_name', 'academic_year')
    search_fields = ('subject__name', 'teacher__first_name', 'teacher__last_name')


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'section', 'subject', 'teacher', 'day_of_week', 'start_time', 'end_time')
    list_filter = ('class_name', 'day_of_week', 'academic_year')
    search_fields = ('subject__name', 'teacher__first_name')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status', 'marked_by')
    list_filter = ('status', 'date')
    search_fields = ('student__admission_number', 'student__user__first_name')
    date_hierarchy = 'date'


@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):
    list_display = ('name', 'exam_type', 'academic_year', 'start_date', 'end_date', 'is_published')
    list_filter = ('exam_type', 'academic_year', 'is_published')
    search_fields = ('name',)
    date_hierarchy = 'start_date'


@admin.register(ExamSchedule)
class ExamScheduleAdmin(admin.ModelAdmin):
    list_display = ('examination', 'class_name', 'subject', 'date', 'start_time', 'total_marks')
    list_filter = ('examination', 'class_name')
    search_fields = ('subject__name',)
    date_hierarchy = 'date'


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam_schedule', 'theory_marks', 'practical_marks', 'total_marks', 'grade')
    list_filter = ('exam_schedule__examination', 'grade', 'is_absent')
    search_fields = ('student__admission_number', 'student__user__first_name')


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'class_name', 'section', 'subject', 'teacher', 'assigned_date', 'due_date')
    list_filter = ('class_name', 'subject', 'assigned_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'assigned_date'


@admin.register(HomeworkSubmission)
class HomeworkSubmissionAdmin(admin.ModelAdmin):
    list_display = ('homework', 'student', 'submission_date', 'marks_obtained', 'graded_by')
    list_filter = ('homework', 'submission_date')
    search_fields = ('student__admission_number', 'homework__title')
