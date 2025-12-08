from django.contrib import admin
from .models import (
    Department, Designation, Staff, StaffAttendance,
    LeaveType, Leave, Performance, StaffDocument
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'head', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'code')


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'code')


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'employee_id', 'get_full_name', 'department', 'designation',
        'employment_type', 'joining_date', 'is_active'
    )
    list_filter = ('employment_type', 'department', 'designation', 'is_active', 'campus')
    search_fields = ('employee_id', 'user__first_name', 'user__last_name', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    
    def get_full_name(self, obj):
        return obj.user.get_full_name()
    get_full_name.short_description = 'Name'


@admin.register(StaffAttendance)
class StaffAttendanceAdmin(admin.ModelAdmin):
    list_display = ('staff', 'date', 'check_in', 'check_out', 'status', 'marked_by')
    list_filter = ('status', 'date')
    search_fields = ('staff__employee_id', 'staff__user__first_name')
    date_hierarchy = 'date'


@admin.register(LeaveType)
class LeaveTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'days_allowed', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'code')


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('staff', 'leave_type', 'start_date', 'end_date', 'total_days', 'status')
    list_filter = ('status', 'leave_type', 'start_date')
    search_fields = ('staff__employee_id', 'staff__user__first_name')
    date_hierarchy = 'start_date'


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('staff', 'review_date', 'overall_rating', 'reviewed_by')
    list_filter = ('review_date',)
    search_fields = ('staff__employee_id', 'staff__user__first_name')
    date_hierarchy = 'review_date'


@admin.register(StaffDocument)
class StaffDocumentAdmin(admin.ModelAdmin):
    list_display = ('staff', 'document_type', 'title', 'uploaded_at')
    list_filter = ('document_type', 'uploaded_at')
    search_fields = ('staff__employee_id', 'title')
