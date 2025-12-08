from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, Campus, AcademicYear, Holiday


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name', 'email', 'phone_number',
            'date_of_birth', 'gender', 'profile_picture'
        )}),
        (_('Address'), {'fields': (
            'address', 'city', 'state', 'country', 'postal_code'
        )}),
        (_('Permissions'), {'fields': (
            'role', 'is_active', 'is_staff', 'is_superuser',
            'groups', 'user_permissions'
        )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_active')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active', 'gender')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
    ordering = ('username',)


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'city', 'principal', 'is_active', 'established_date')
    list_filter = ('is_active', 'city', 'country')
    search_fields = ('name', 'code', 'city', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('name', 'code', 'logo', 'principal', 'is_active', 'established_date')
        }),
        (_('Contact Information'), {
            'fields': ('address', 'city', 'state', 'country', 'postal_code', 'phone', 'email')
        }),
        (_('Timestamps'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('name', 'campus', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current', 'campus')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'start_date'


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'end_date', 'campus', 'academic_year')
    list_filter = ('campus', 'academic_year')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'date'
