from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User, Campus


class Hostel(models.Model):
    """Hostel/Dormitory Management"""
    
    class HostelType(models.TextChoices):
        BOYS = 'BOYS', _('Boys Hostel')
        GIRLS = 'GIRLS', _('Girls Hostel')
    
    name = models.CharField(max_length=200)
    hostel_type = models.CharField(
        max_length=10,
        choices=HostelType.choices
    )
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
        related_name='hostels'
    )
    warden = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='hostel_warden',
        limit_choices_to={'role': 'HOSTEL_WARDEN'}
    )
    address = models.TextField()
    total_rooms = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'hostels'
        verbose_name = _('Hostel')
        verbose_name_plural = _('Hostels')
    
    def __str__(self):
        return f"{self.name} ({self.get_hostel_type_display()})"


class Room(models.Model):
    """Hostel Room Management"""
    
    class RoomType(models.TextChoices):
        SINGLE = 'SINGLE', _('Single')
        DOUBLE = 'DOUBLE', _('Double')
        TRIPLE = 'TRIPLE', _('Triple')
        DORMITORY = 'DORMITORY', _('Dormitory')
    
    hostel = models.ForeignKey(
        Hostel,
        on_delete=models.CASCADE,
        related_name='rooms'
    )
    room_number = models.CharField(max_length=50)
    room_type = models.CharField(
        max_length=20,
        choices=RoomType.choices
    )
    capacity = models.IntegerField()
    floor = models.IntegerField()
    monthly_fee = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'hostel_rooms'
        verbose_name = _('Hostel Room')
        verbose_name_plural = _('Hostel Rooms')
        unique_together = ['hostel', 'room_number']
    
    def __str__(self):
        return f"{self.hostel.name} - Room {self.room_number}"
    
    @property
    def current_occupancy(self):
        return self.students.filter(status='ACTIVE').count()
    
    @property
    def is_full(self):
        return self.current_occupancy >= self.capacity


class HostelFacility(models.Model):
    """Hostel Facilities Management"""
    hostel = models.ForeignKey(
        Hostel,
        on_delete=models.CASCADE,
        related_name='facilities'
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'hostel_facilities'
        verbose_name = _('Hostel Facility')
        verbose_name_plural = _('Hostel Facilities')
    
    def __str__(self):
        return f"{self.hostel.name} - {self.name}"


class HostelComplaint(models.Model):
    """Hostel Complaints Management"""
    
    class ComplaintStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        IN_PROGRESS = 'IN_PROGRESS', _('In Progress')
        RESOLVED = 'RESOLVED', _('Resolved')
        CLOSED = 'CLOSED', _('Closed')
    
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='hostel_complaints'
    )
    hostel = models.ForeignKey(
        Hostel,
        on_delete=models.CASCADE,
        related_name='complaints'
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='complaints',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=ComplaintStatus.choices,
        default=ComplaintStatus.PENDING
    )
    filed_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(null=True, blank=True)
    resolved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='resolved_complaints'
    )
    resolution_remarks = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'hostel_complaints'
        verbose_name = _('Hostel Complaint')
        verbose_name_plural = _('Hostel Complaints')
        ordering = ['-filed_date']
    
    def __str__(self):
        return f"{self.title} - {self.student.admission_number}"
