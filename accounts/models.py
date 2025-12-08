from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Custom User Model with role-based access"""
    
    class UserRole(models.TextChoices):
        SUPER_ADMIN = 'SUPER_ADMIN', _('Super Admin')
        ADMIN = 'ADMIN', _('Admin')
        TEACHER = 'TEACHER', _('Teacher')
        STUDENT = 'STUDENT', _('Student')
        PARENT = 'PARENT', _('Parent')
        ACCOUNTANT = 'ACCOUNTANT', _('Accountant')
        LIBRARIAN = 'LIBRARIAN', _('Librarian')
        RECEPTIONIST = 'RECEPTIONIST', _('Receptionist')
        DRIVER = 'DRIVER', _('Driver')
        HOSTEL_WARDEN = 'HOSTEL_WARDEN', _('Hostel Warden')
    
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.STUDENT
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        blank=True,
        null=True
    )
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"
    
    @property
    def is_admin(self):
        return self.role in [self.UserRole.SUPER_ADMIN, self.UserRole.ADMIN]
    
    @property
    def is_teacher(self):
        return self.role == self.UserRole.TEACHER
    
    @property
    def is_student(self):
        return self.role == self.UserRole.STUDENT
    
    @property
    def is_parent(self):
        return self.role == self.UserRole.PARENT


class Campus(models.Model):
    """Multi-campus/branch support"""
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    principal = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='campus_principal'
    )
    is_active = models.BooleanField(default=True)
    established_date = models.DateField(blank=True, null=True)
    logo = models.ImageField(upload_to='campus_logos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'campuses'
        verbose_name = _('Campus')
        verbose_name_plural = _('Campuses')
    
    def __str__(self):
        return self.name


class AcademicYear(models.Model):
    """Academic Year Management"""
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
        related_name='academic_years'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'academic_years'
        verbose_name = _('Academic Year')
        verbose_name_plural = _('Academic Years')
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.name} ({self.campus.name})"
    
    def save(self, *args, **kwargs):
        if self.is_current:
            # Set all other academic years for this campus to not current
            AcademicYear.objects.filter(
                campus=self.campus,
                is_current=True
            ).exclude(pk=self.pk).update(is_current=False)
        super().save(*args, **kwargs)


class Holiday(models.Model):
    """Holiday Management"""
    name = models.CharField(max_length=200)
    date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        related_name='holidays'
    )
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
        related_name='holidays'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'holidays'
        verbose_name = _('Holiday')
        verbose_name_plural = _('Holidays')
        ordering = ['date']
    
    def __str__(self):
        return f"{self.name} - {self.date}"
