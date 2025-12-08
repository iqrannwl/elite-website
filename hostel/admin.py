from django.contrib import admin
from .models import Hostel, Room, HostelFacility, HostelComplaint


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ('name', 'hostel_type', 'campus', 'warden', 'total_rooms', 'is_active')
    list_filter = ('hostel_type', 'campus', 'is_active')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'room_number', 'hostel', 'room_type', 'floor',
        'capacity', 'current_occupancy', 'monthly_fee', 'is_active'
    )
    list_filter = ('hostel', 'room_type', 'floor', 'is_active')
    search_fields = ('room_number',)
    readonly_fields = ('created_at', 'updated_at', 'current_occupancy')


@admin.register(HostelFacility)
class HostelFacilityAdmin(admin.ModelAdmin):
    list_display = ('hostel', 'name', 'is_available')
    list_filter = ('hostel', 'is_available')
    search_fields = ('name',)


@admin.register(HostelComplaint)
class HostelComplaintAdmin(admin.ModelAdmin):
    list_display = ('student', 'hostel', 'title', 'status', 'filed_date', 'resolved_date')
    list_filter = ('status', 'hostel', 'filed_date')
    search_fields = ('title', 'student__admission_number')
    date_hierarchy = 'filed_date'
