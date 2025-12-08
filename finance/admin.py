from django.contrib import admin
from .models import (
    FeeType, FeeStructure, FeeInvoice, FeeInvoiceItem,
    Payment, Discount, StudentDiscount, Expense, Salary
)


@admin.register(FeeType)
class FeeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'code')


@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'fee_type', 'amount', 'frequency', 'academic_year', 'is_active')
    list_filter = ('frequency', 'academic_year', 'is_active')
    search_fields = ('class_name__name', 'fee_type__name')


@admin.register(FeeInvoice)
class FeeInvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'invoice_number', 'student', 'invoice_date', 'due_date',
        'total_amount', 'paid_amount', 'balance_amount', 'status'
    )
    list_filter = ('status', 'invoice_date', 'academic_year')
    search_fields = ('invoice_number', 'student__admission_number')
    readonly_fields = ('created_at', 'updated_at', 'balance_amount')
    date_hierarchy = 'invoice_date'


@admin.register(FeeInvoiceItem)
class FeeInvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'fee_type', 'amount')
    list_filter = ('fee_type',)
    search_fields = ('invoice__invoice_number',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'receipt_number', 'invoice', 'payment_date', 'amount',
        'payment_method', 'payment_status', 'received_by'
    )
    list_filter = ('payment_method', 'payment_status', 'payment_date')
    search_fields = ('receipt_number', 'invoice__invoice_number', 'transaction_id')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'payment_date'


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'discount_type', 'value', 'is_active')
    list_filter = ('discount_type', 'is_active')
    search_fields = ('name', 'code')


@admin.register(StudentDiscount)
class StudentDiscountAdmin(admin.ModelAdmin):
    list_display = ('student', 'discount', 'academic_year', 'approved_by', 'is_active')
    list_filter = ('discount', 'academic_year', 'is_active')
    search_fields = ('student__admission_number',)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'amount', 'date', 'payment_method', 'is_approved')
    list_filter = ('category', 'payment_method', 'is_approved', 'date')
    search_fields = ('title', 'paid_to')
    date_hierarchy = 'date'


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('staff', 'month', 'year', 'basic_salary', 'net_salary', 'status', 'payment_date')
    list_filter = ('status', 'year', 'month')
    search_fields = ('staff__employee_id', 'staff__user__first_name')
    readonly_fields = ('created_at', 'updated_at', 'net_salary')
