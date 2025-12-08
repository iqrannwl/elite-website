from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User, Campus


class Department(models.Model):
    """Department Management"""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    head = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='department_head'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'departments'
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
    
    def __str__(self):
        return self.name


class Designation(models.Model):
    """Designation/Position Management"""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'designations'
        verbose_name = _('Designation')
        verbose_name_plural = _('Designations')
    
    def __str__(self):
        return self.name


class Staff(models.Model):
    """Staff/Employee Management"""
    
    class EmploymentType(models.TextChoices):
        PERMANENT = 'PERMANENT', _('Permanent')
        CONTRACT = 'CONTRACT', _('Contract')
        TEMPORARY = 'TEMPORARY', _('Temporary')
        PART_TIME = 'PART_TIME', _('Part Time')
    
    class MaritalStatus(models.TextChoices):
        SINGLE = 'SINGLE', _('Single')
        MARRIED = 'MARRIED', _('Married')
        DIVORCED = 'DIVORCED', _('Divorced')
        WIDOWED = 'WIDOWED', _('Widowed')
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='staff_profile'
    )
    employee_id = models.CharField(max_length=50, unique=True)
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
        related_name='staff'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        related_name='staff'
    )
    designation = models.ForeignKey(
        Designation,
        on_delete=models.SET_NULL,
        null=True,
        related_name='staff'
    )
    
    # Employment Details
    employment_type = models.CharField(
        max_length=20,
        choices=EmploymentType.choices,
        default=EmploymentType.PERMANENT
    )
    joining_date = models.DateField()
    leaving_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    # Personal Information
    marital_status = models.CharField(
        max_length=20,
        choices=MaritalStatus.choices,
        blank=True,
        null=True
    )
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    nationality = models.CharField(max_length=50, default='Pakistani')
    religion = models.CharField(max_length=50, blank=True, null=True)
    
    # Contact Information
    emergency_contact_name = models.CharField(max_length=200)
    emergency_contact_phone = models.CharField(max_length=20)
    emergency_contact_relation = models.CharField(max_length=50)
    
    # Salary Information
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    bank_account_number = models.CharField(max_length=50, blank=True, null=True)
    bank_ifsc_code = models.CharField(max_length=20, blank=True, null=True)
    
    # Qualification
    qualification = models.CharField(max_length=200, blank=True, null=True)
    experience_years = models.IntegerField(default=0)
    
    # Documents
    resume = models.FileField(upload_to='staff_documents/resumes/', blank=True, null=True)
    id_proof = models.FileField(upload_to='staff_documents/id_proofs/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'staff'
        verbose_name = _('Staff')
        verbose_name_plural = _('Staff')
        ordering = ['employee_id']
    
    def __str__(self):
        return f"{self.employee_id} - {self.user.get_full_name()}"


class StaffAttendance(models.Model):
    """Staff Attendance Management"""
    
    class AttendanceStatus(models.TextChoices):
        PRESENT = 'PRESENT', _('Present')
        ABSENT = 'ABSENT', _('Absent')
        LATE = 'LATE', _('Late')
        HALF_DAY = 'HALF_DAY', _('Half Day')
        LEAVE = 'LEAVE', _('Leave')
        HOLIDAY = 'HOLIDAY', _('Holiday')
    
    staff = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )
    date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
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
        related_name='marked_staff_attendance'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'staff_attendance'
        verbose_name = _('Staff Attendance')
        verbose_name_plural = _('Staff Attendance Records')
        unique_together = ['staff', 'date']
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.staff.employee_id} - {self.date} - {self.status}"


class LeaveType(models.Model):
    """Leave Type Management"""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    days_allowed = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leave_types'
        verbose_name = _('Leave Type')
        verbose_name_plural = _('Leave Types')
    
    def __str__(self):
        return self.name


class Leave(models.Model):
    """Leave Management"""
    
    class LeaveStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        APPROVED = 'APPROVED', _('Approved')
        REJECTED = 'REJECTED', _('Rejected')
        CANCELLED = 'CANCELLED', _('Cancelled')
    
    staff = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name='leaves'
    )
    leave_type = models.ForeignKey(
        LeaveType,
        on_delete=models.CASCADE,
        related_name='leaves'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    total_days = models.IntegerField()
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=LeaveStatus.choices,
        default=LeaveStatus.PENDING
    )
    applied_on = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_leaves'
    )
    approved_on = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'leaves'
        verbose_name = _('Leave')
        verbose_name_plural = _('Leaves')
        ordering = ['-applied_on']
    
    def __str__(self):
        return f"{self.staff.employee_id} - {self.leave_type.name} - {self.start_date}"


class Performance(models.Model):
    """Staff Performance Tracking"""
    staff = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name='performance_records'
    )
    review_date = models.DateField()
    review_period_start = models.DateField()
    review_period_end = models.DateField()
    
    # Rating (1-5 scale)
    punctuality = models.IntegerField(default=3)
    teaching_quality = models.IntegerField(default=3, null=True, blank=True)
    communication = models.IntegerField(default=3)
    teamwork = models.IntegerField(default=3)
    discipline = models.IntegerField(default=3)
    overall_rating = models.DecimalField(max_digits=3, decimal_places=2, default=3.0)
    
    strengths = models.TextField(blank=True, null=True)
    weaknesses = models.TextField(blank=True, null=True)
    recommendations = models.TextField(blank=True, null=True)
    
    reviewed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='conducted_reviews'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'performance_reviews'
        verbose_name = _('Performance Review')
        verbose_name_plural = _('Performance Reviews')
        ordering = ['-review_date']
    
    def __str__(self):
        return f"{self.staff.employee_id} - {self.review_date}"
    
    def save(self, *args, **kwargs):
        # Calculate overall rating
        ratings = [self.punctuality, self.communication, self.teamwork, self.discipline]
        if self.teaching_quality:
            ratings.append(self.teaching_quality)
        self.overall_rating = sum(ratings) / len(ratings)
        super().save(*args, **kwargs)


class StaffDocument(models.Model):
    """Staff Documents Management"""
    
    class DocumentType(models.TextChoices):
        RESUME = 'RESUME', _('Resume')
        ID_PROOF = 'ID_PROOF', _('ID Proof')
        CERTIFICATE = 'CERTIFICATE', _('Certificate')
        EXPERIENCE_LETTER = 'EXPERIENCE_LETTER', _('Experience Letter')
        OTHER = 'OTHER', _('Other')
    
    staff = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name='documents'
    )
    document_type = models.CharField(
        max_length=30,
        choices=DocumentType.choices
    )
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='staff_documents/')
    description = models.TextField(blank=True, null=True)
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='uploaded_staff_documents'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'staff_documents'
        verbose_name = _('Staff Document')
        verbose_name_plural = _('Staff Documents')
    
    def __str__(self):
        return f"{self.staff.employee_id} - {self.title}"
