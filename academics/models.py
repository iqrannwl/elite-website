from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User, Campus, AcademicYear


class Class(models.Model):
    """Class/Grade Management"""
    name = models.CharField(max_length=100)
    numeric_value = models.IntegerField(help_text="For sorting (e.g., 1 for Class 1, 10 for Class 10)")
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
        related_name='classes'
    )
    class_teacher = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='class_teacher_of',
        limit_choices_to={'role': 'TEACHER'}
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'classes'
        verbose_name = _('Class')
        verbose_name_plural = _('Classes')
        ordering = ['numeric_value']
        unique_together = ['name', 'campus']
    
    def __str__(self):
        return f"{self.name} ({self.campus.name})"


class Section(models.Model):
    """Section Management (e.g., A, B, C)"""
    name = models.CharField(max_length=50)
    class_name = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name='sections'
    )
    capacity = models.IntegerField(default=40)
    room_number = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'sections'
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        unique_together = ['name', 'class_name']
    
    def __str__(self):
        return f"{self.class_name.name} - {self.name}"
    
    @property
    def current_strength(self):
        return self.students.filter(status='ACTIVE').count()


class Subject(models.Model):
    """Subject Management"""
    
    class SubjectType(models.TextChoices):
        THEORY = 'THEORY', _('Theory')
        PRACTICAL = 'PRACTICAL', _('Practical')
        BOTH = 'BOTH', _('Both')
    
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    subject_type = models.CharField(
        max_length=20,
        choices=SubjectType.choices,
        default=SubjectType.THEORY
    )
    description = models.TextField(blank=True, null=True)
    is_elective = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'subjects'
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')
    
    def __str__(self):
        return f"{self.code} - {self.name}"


class ClassSubject(models.Model):
    """Subject Assignment to Classes"""
    class_name = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name='class_subjects'
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='assigned_classes'
    )
    teacher = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='teaching_subjects',
        limit_choices_to={'role': 'TEACHER'}
    )
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        related_name='class_subjects'
    )
    theory_marks = models.IntegerField(default=100)
    practical_marks = models.IntegerField(default=0)
    pass_marks = models.IntegerField(default=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'class_subjects'
        verbose_name = _('Class Subject')
        verbose_name_plural = _('Class Subjects')
        unique_together = ['class_name', 'subject', 'academic_year']
    
    def __str__(self):
        return f"{self.class_name.name} - {self.subject.name}"


class Timetable(models.Model):
    """Timetable/Schedule Management"""
    
    class DayOfWeek(models.TextChoices):
        MONDAY = 'MONDAY', _('Monday')
        TUESDAY = 'TUESDAY', _('Tuesday')
        WEDNESDAY = 'WEDNESDAY', _('Wednesday')
        THURSDAY = 'THURSDAY', _('Thursday')
        FRIDAY = 'FRIDAY', _('Friday')
        SATURDAY = 'SATURDAY', _('Saturday')
        SUNDAY = 'SUNDAY', _('Sunday')
    
    class_name = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name='timetables'
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='timetables'
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='timetables'
    )
    teacher = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='timetable_slots',
        limit_choices_to={'role': 'TEACHER'}
    )
    day_of_week = models.CharField(
        max_length=10,
        choices=DayOfWeek.choices
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_number = models.CharField(max_length=50, blank=True, null=True)
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        related_name='timetables'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'timetables'
        verbose_name = _('Timetable')
        verbose_name_plural = _('Timetables')
        ordering = ['day_of_week', 'start_time']
    
    def __str__(self):
        return f"{self.class_name.name}-{self.section.name} | {self.day_of_week} | {self.subject.name}"


class Attendance(models.Model):
    """Attendance Management for Students"""
    
    class AttendanceStatus(models.TextChoices):
        PRESENT = 'PRESENT', _('Present')
        ABSENT = 'ABSENT', _('Absent')
        LATE = 'LATE', _('Late')
        HALF_DAY = 'HALF_DAY', _('Half Day')
        LEAVE = 'LEAVE', _('Leave')
    
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=AttendanceStatus.choices,
        default=AttendanceStatus.PRESENT
    )
    remarks = models.TextField(blank=True, null=True)
    marked_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='marked_attendance'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'attendance'
        verbose_name = _('Attendance')
        verbose_name_plural = _('Attendance Records')
        unique_together = ['student', 'date']
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.student.admission_number} - {self.date} - {self.status}"


class Examination(models.Model):
    """Examination Management"""
    
    class ExamType(models.TextChoices):
        MONTHLY = 'MONTHLY', _('Monthly Test')
        QUARTERLY = 'QUARTERLY', _('Quarterly')
        HALF_YEARLY = 'HALF_YEARLY', _('Half Yearly')
        ANNUAL = 'ANNUAL', _('Annual')
        FINAL = 'FINAL', _('Final')
    
    name = models.CharField(max_length=200)
    exam_type = models.CharField(
        max_length=20,
        choices=ExamType.choices
    )
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        related_name='examinations'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'examinations'
        verbose_name = _('Examination')
        verbose_name_plural = _('Examinations')
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.name} ({self.academic_year.name})"


class ExamSchedule(models.Model):
    """Exam Schedule/Timetable"""
    examination = models.ForeignKey(
        Examination,
        on_delete=models.CASCADE,
        related_name='schedules'
    )
    class_name = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name='exam_schedules'
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='exam_schedules'
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_number = models.CharField(max_length=50, blank=True, null=True)
    total_marks = models.IntegerField()
    pass_marks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'exam_schedules'
        verbose_name = _('Exam Schedule')
        verbose_name_plural = _('Exam Schedules')
        ordering = ['date', 'start_time']
    
    def __str__(self):
        return f"{self.examination.name} - {self.class_name.name} - {self.subject.name}"


class Grade(models.Model):
    """Student Grades/Marks"""
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='grades'
    )
    exam_schedule = models.ForeignKey(
        ExamSchedule,
        on_delete=models.CASCADE,
        related_name='grades'
    )
    theory_marks = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    practical_marks = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    grade = models.CharField(max_length=5, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    is_absent = models.BooleanField(default=False)
    entered_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='entered_grades'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'grades'
        verbose_name = _('Grade')
        verbose_name_plural = _('Grades')
        unique_together = ['student', 'exam_schedule']
    
    def __str__(self):
        return f"{self.student.admission_number} - {self.exam_schedule.subject.name} - {self.total_marks}"
    
    def save(self, *args, **kwargs):
        self.total_marks = self.theory_marks + self.practical_marks
        # Calculate grade based on percentage
        percentage = (self.total_marks / self.exam_schedule.total_marks) * 100
        if percentage >= 90:
            self.grade = 'A+'
        elif percentage >= 80:
            self.grade = 'A'
        elif percentage >= 70:
            self.grade = 'B'
        elif percentage >= 60:
            self.grade = 'C'
        elif percentage >= 50:
            self.grade = 'D'
        else:
            self.grade = 'F'
        super().save(*args, **kwargs)


class Homework(models.Model):
    """Homework/Assignment Management"""
    
    class Status(models.TextChoices):
        ASSIGNED = 'ASSIGNED', _('Assigned')
        SUBMITTED = 'SUBMITTED', _('Submitted')
        GRADED = 'GRADED', _('Graded')
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    class_name = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name='homework'
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='homework'
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='homework'
    )
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assigned_homework',
        limit_choices_to={'role': 'TEACHER'}
    )
    assigned_date = models.DateField()
    due_date = models.DateField()
    attachment = models.FileField(upload_to='homework/', blank=True, null=True)
    max_marks = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'homework'
        verbose_name = _('Homework')
        verbose_name_plural = _('Homework')
        ordering = ['-assigned_date']
    
    def __str__(self):
        return f"{self.title} - {self.class_name.name}"


class HomeworkSubmission(models.Model):
    """Student Homework Submissions"""
    homework = models.ForeignKey(
        Homework,
        on_delete=models.CASCADE,
        related_name='submissions'
    )
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='homework_submissions'
    )
    submission_date = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to='homework_submissions/')
    remarks = models.TextField(blank=True, null=True)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    teacher_remarks = models.TextField(blank=True, null=True)
    graded_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='graded_homework'
    )
    graded_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'homework_submissions'
        verbose_name = _('Homework Submission')
        verbose_name_plural = _('Homework Submissions')
        unique_together = ['homework', 'student']
    
    def __str__(self):
        return f"{self.homework.title} - {self.student.admission_number}"
