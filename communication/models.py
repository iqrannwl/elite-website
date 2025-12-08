from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User, Campus, AcademicYear


class Announcement(models.Model):
    """Announcement Management"""
    
    class AnnouncementType(models.TextChoices):
        GENERAL = 'GENERAL', _('General')
        URGENT = 'URGENT', _('Urgent')
        EVENT = 'EVENT', _('Event')
        HOLIDAY = 'HOLIDAY', _('Holiday')
        EXAM = 'EXAM', _('Examination')
    
    class TargetAudience(models.TextChoices):
        ALL = 'ALL', _('All')
        STUDENTS = 'STUDENTS', _('Students')
        TEACHERS = 'TEACHERS', _('Teachers')
        PARENTS = 'PARENTS', _('Parents')
        STAFF = 'STAFF', _('Staff')
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    announcement_type = models.CharField(
        max_length=20,
        choices=AnnouncementType.choices,
        default=AnnouncementType.GENERAL
    )
    target_audience = models.CharField(
        max_length=20,
        choices=TargetAudience.choices,
        default=TargetAudience.ALL
    )
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
        related_name='announcements'
    )
    class_name = models.ForeignKey(
        'academics.Class',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='announcements',
        help_text="Leave blank for all classes"
    )
    attachment = models.FileField(upload_to='announcements/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_announcements'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'announcements'
        verbose_name = _('Announcement')
        verbose_name_plural = _('Announcements')
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Message(models.Model):
    """Internal Messaging System"""
    
    class MessageStatus(models.TextChoices):
        SENT = 'SENT', _('Sent')
        DELIVERED = 'DELIVERED', _('Delivered')
        READ = 'READ', _('Read')
    
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )
    subject = models.CharField(max_length=200)
    message = models.TextField()
    attachment = models.FileField(upload_to='messages/', blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=MessageStatus.choices,
        default=MessageStatus.SENT
    )
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    parent_message = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'messages'
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.sender.get_full_name()} to {self.recipient.get_full_name()} - {self.subject}"


class Notification(models.Model):
    """Notification System"""
    
    class NotificationType(models.TextChoices):
        INFO = 'INFO', _('Information')
        WARNING = 'WARNING', _('Warning')
        SUCCESS = 'SUCCESS', _('Success')
        ERROR = 'ERROR', _('Error')
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    title = models.CharField(max_length=200)
    message = models.TextField()
    notification_type = models.CharField(
        max_length=20,
        choices=NotificationType.choices,
        default=NotificationType.INFO
    )
    link = models.CharField(max_length=500, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'notifications'
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.title}"


class SMSLog(models.Model):
    """SMS Notification Log"""
    
    class SMSStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        SENT = 'SENT', _('Sent')
        FAILED = 'FAILED', _('Failed')
    
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sms_logs'
    )
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=SMSStatus.choices,
        default=SMSStatus.PENDING
    )
    sent_at = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'sms_logs'
        verbose_name = _('SMS Log')
        verbose_name_plural = _('SMS Logs')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.phone_number} - {self.status}"


class EmailLog(models.Model):
    """Email Notification Log"""
    
    class EmailStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        SENT = 'SENT', _('Sent')
        FAILED = 'FAILED', _('Failed')
    
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='email_logs'
    )
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=EmailStatus.choices,
        default=EmailStatus.PENDING
    )
    sent_at = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'email_logs'
        verbose_name = _('Email Log')
        verbose_name_plural = _('Email Logs')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.email} - {self.subject}"
