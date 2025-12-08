from django.contrib import admin
from .models import (
    Student, StudentDocument, StudentHealthRecord,
    StudentPromotion, Sibling
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'admission_number', 'get_full_name', 'current_class',
        'section', 'campus', 'status', 'admission_date'
    )
    list_filter = ('status', 'campus', 'current_class', 'user__gender', 'blood_group')
    search_fields = (
        'admission_number', 'user__first_name', 'user__last_name',
        'user__email', 'father_name', 'mother_name'
    )
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('User Account', {
            'fields': ('user', 'admission_number', 'admission_date', 'status')
        }),
        ('Academic Information', {
            'fields': ('campus', 'current_class', 'section', 'roll_number')
        }),
        ('Personal Information', {
            'fields': ('blood_group', 'religion', 'caste', 'nationality')
        }),
        ('Father Information', {
            'fields': ('father_name', 'father_phone', 'father_occupation', 'father_email')
        }),
        ('Mother Information', {
            'fields': ('mother_name', 'mother_phone', 'mother_occupation', 'mother_email')
        }),
        ('Guardian Information', {
            'fields': ('guardian_name', 'guardian_phone', 'guardian_relation', 'guardian_email')
        }),
        ('Emergency Contact', {
            'fields': ('emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_relation')
        }),
        ('Previous School', {
            'fields': ('previous_school', 'previous_class')
        }),
        ('Medical Information', {
            'fields': ('medical_conditions', 'allergies', 'medications')
        }),
        ('Transport & Hostel', {
            'fields': ('uses_transport', 'route', 'is_hosteler', 'hostel_room')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_full_name(self, obj):
        return obj.user.get_full_name()
    get_full_name.short_description = 'Name'


@admin.register(StudentDocument)
class StudentDocumentAdmin(admin.ModelAdmin):
    list_display = ('student', 'document_type', 'title', 'uploaded_at')
    list_filter = ('document_type', 'uploaded_at')
    search_fields = ('student__admission_number', 'title')
    readonly_fields = ('uploaded_at',)


@admin.register(StudentHealthRecord)
class StudentHealthRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'height', 'weight', 'bmi', 'doctor_name')
    list_filter = ('date',)
    search_fields = ('student__admission_number', 'doctor_name')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(StudentPromotion)
class StudentPromotionAdmin(admin.ModelAdmin):
    list_display = ('student', 'from_class', 'to_class', 'academic_year', 'promotion_date')
    list_filter = ('academic_year', 'promotion_date')
    search_fields = ('student__admission_number',)
    readonly_fields = ('created_at',)


@admin.register(Sibling)
class SiblingAdmin(admin.ModelAdmin):
    list_display = ('get_student1_name', 'get_student2_name', 'relation')
    list_filter = ('relation',)
    search_fields = (
        'student1__admission_number', 'student2__admission_number',
        'student1__user__first_name', 'student2__user__first_name'
    )
    
    def get_student1_name(self, obj):
        return obj.student1.user.get_full_name()
    get_student1_name.short_description = 'Student 1'
    
    def get_student2_name(self, obj):
        return obj.student2.user.get_full_name()
    get_student2_name.short_description = 'Student 2'
