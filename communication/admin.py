from django.contrib import admin
from .models import Announcement, Message, Notification, SMSLog, EmailLog


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'announcement_type', 'target_audience',
        'campus', 'start_date', 'end_date', 'is_active'
    )
    list_filter = ('announcement_type', 'target_audience', 'campus', 'is_active')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'start_date'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'subject', 'status', 'is_read', 'created_at')
    list_filter = ('status', 'is_read', 'created_at')
    search_fields = ('subject', 'sender__first_name', 'recipient__first_name')
    readonly_fields = ('created_at',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'notification_type', 'is_read', 'created_at')
    list_filter = ('notification_type', 'is_read', 'created_at')
    search_fields = ('title', 'user__first_name', 'user__last_name')
    readonly_fields = ('created_at',)


@admin.register(SMSLog)
class SMSLogAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'phone_number', 'status', 'sent_at', 'created_at')
    list_filter = ('status', 'sent_at')
    search_fields = ('phone_number', 'recipient__first_name')
    readonly_fields = ('created_at',)


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'email', 'subject', 'status', 'sent_at', 'created_at')
    list_filter = ('status', 'sent_at')
    search_fields = ('email', 'subject', 'recipient__first_name')
    readonly_fields = ('created_at',)
