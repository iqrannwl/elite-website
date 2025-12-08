from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User, Campus, AcademicYear


class Student(models.Model):
    """Student Information System"""
    
    class BloodGroup(models.TextChoices):
        A_POSITIVE = 'A+', _('A+')
        A_NEGATIVE = 'A-', _('A-')
        B_POSITIVE = 'B+', _('B+')
        B_NEGATIVE = 'B-', _('B-')
        O_POSITIVE = 'O+', _('O+')
        O_NEGATIVE = 'O-', _('O-')
        AB_POSITIVE = 'AB+', _('AB+')
        AB_NEGATIVE = 'AB-', _('AB-')
    
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', _('Active')
        INACTIVE = 'INACTIVE', _('Inactive')
        GRADUATED = 'GRADUATED', _('Graduated')
        TRANSFERRED = 'TRANSFERRED', _('Transferred')
        EXPELLED = 'EXPELLED', _('Expelled')
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )
    admission_number = models.CharField(max_length=50, unique=True)
    admission_date = models.DateField()
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
        related_name='students'
    )
    current_class = models.ForeignKey(
        'academics.Class',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='current_students'
    )
    section = models.ForeignKey(
        'academics.Section',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students'
    )
    roll_number = models.CharField(max_length=20, blank=True, null=True)
    
    # Personal Information
    blood_group = models.CharField(
        max_length=3,
        choices=BloodGroup.choices,
        blank=True,
        null=True
    )
    religion = models.CharField(max_length=50, blank=True, null=True)
    caste = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=50, default='Pakistani')
    
    # Parent/Guardian Information
    father_name = models.CharField(max_length=200)
    father_phone = models.CharField(max_length=20)
    father_occupation = models.CharField(max_length=100, blank=True, null=True)
    father_email = models.EmailField(blank=True, null=True)
    
    mother_name = models.CharField(max_length=200)
    mother_phone = models.CharField(max_length=20, blank=True, null=True)
    mother_occupation = models.CharField(max_length=100, blank=True, null=True)
    mother_email = models.EmailField(blank=True, null=True)
    
    guardian_name = models.CharField(max_length=200, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_relation = models.CharField(max_length=50, blank=True, null=True)
    guardian_email = models.EmailField(blank=True, null=True)
    
    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=200)
    emergency_contact_phone = models.CharField(max_length=20)
    emergency_contact_relation = models.CharField(max_length=50)
    
    # Previous School Information
    previous_school = models.CharField(max_length=200, blank=True, null=True)
    previous_class = models.CharField(max_length=50, blank=True, null=True)
    
    # Medical Information
    medical_conditions = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    
    # Status
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    
    # Transport
    uses_transport = models.BooleanField(default=False)
    route = models.ForeignKey(
        'transport.Route',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students'
    )
    
    # Hostel
    is_hosteler = models.BooleanField(default=False)
    hostel_room = models.ForeignKey(
        'hostel.Room',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'students'
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
        ordering = ['admission_number']
    
    def __str__(self):
        return f"{self.admission_number} - {self.user.get_full_name()}"


class StudentDocument(models.Model):
    """Student Documents Management"""
    
    class DocumentType(models.TextChoices):
        BIRTH_CERTIFICATE = 'BIRTH_CERTIFICATE', _('Birth Certificate')
        TRANSFER_CERTIFICATE = 'TRANSFER_CERTIFICATE', _('Transfer Certificate')
        MARKSHEET = 'MARKSHEET', _('Marksheet')
        ID_PROOF = 'ID_PROOF', _('ID Proof')
        PHOTO = 'PHOTO', _('Photo')
        OTHER = 'OTHER', _('Other')
    
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='documents'
    )
    document_type = models.CharField(
        max_length=30,
        choices=DocumentType.choices
    )
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='student_documents/')
    description = models.TextField(blank=True, null=True)
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='uploaded_student_documents'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'student_documents'
        verbose_name = _('Student Document')
        verbose_name_plural = _('Student Documents')
    
    def __str__(self):
        return f"{self.student.admission_number} - {self.title}"


class StudentHealthRecord(models.Model):
    """Student Health Records"""
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='health_records'
    )
    date = models.DateField()
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="in cm")
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="in kg")
    bmi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    blood_pressure = models.CharField(max_length=20, blank=True, null=True)
    temperature = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    doctor_name = models.CharField(max_length=200, blank=True, null=True)
    next_checkup_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_health_records'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'student_health_records'
        verbose_name = _('Student Health Record')
        verbose_name_plural = _('Student Health Records')
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.student.admission_number} - {self.date}"


class StudentPromotion(models.Model):
    """Student Promotion System"""
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='promotions'
    )
    from_class = models.ForeignKey(
        'academics.Class',
        on_delete=models.CASCADE,
        related_name='promoted_from'
    )
    to_class = models.ForeignKey(
        'academics.Class',
        on_delete=models.CASCADE,
        related_name='promoted_to'
    )
    from_section = models.ForeignKey(
        'academics.Section',
        on_delete=models.CASCADE,
        related_name='promoted_from_section',
        null=True,
        blank=True
    )
    to_section = models.ForeignKey(
        'academics.Section',
        on_delete=models.CASCADE,
        related_name='promoted_to_section',
        null=True,
        blank=True
    )
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        related_name='promotions'
    )
    promotion_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    promoted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='student_promotions'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'student_promotions'
        verbose_name = _('Student Promotion')
        verbose_name_plural = _('Student Promotions')
        ordering = ['-promotion_date']
    
    def __str__(self):
        return f"{self.student.admission_number} - {self.from_class} to {self.to_class}"


class Sibling(models.Model):
    """Sibling Management"""
    student1 = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='siblings_as_student1'
    )
    student2 = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='siblings_as_student2'
    )
    relation = models.CharField(
        max_length=50,
        choices=[
            ('BROTHER', 'Brother'),
            ('SISTER', 'Sister'),
            ('TWIN', 'Twin')
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'siblings'
        verbose_name = _('Sibling')
        verbose_name_plural = _('Siblings')
        unique_together = ['student1', 'student2']
    
    def __str__(self):
        return f"{self.student1.user.get_full_name()} - {self.student2.user.get_full_name()}"
