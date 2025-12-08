from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User, AcademicYear
from decimal import Decimal


class FeeType(models.Model):
    """Fee Type Management (Tuition, Transport, Library, etc.)"""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'fee_types'
        verbose_name = _('Fee Type')
        verbose_name_plural = _('Fee Types')
    
    def __str__(self):
        return self.name


class FeeStructure(models.Model):
    """Fee Structure for Different Classes"""
    
    class FeeFrequency(models.TextChoices):
        MONTHLY = 'MONTHLY', _('Monthly')
        QUARTERLY = 'QUARTERLY', _('Quarterly')
        HALF_YEARLY = 'HALF_YEARLY', _('Half Yearly')
        ANNUALLY = 'ANNUALLY', _('Annually')
        ONE_TIME = 'ONE_TIME', _('One Time')
    
    class_name = models.ForeignKey(
        'academics.Class',
        on_delete=models.CASCADE,
        related_name='fee_structures'
    )
    fee_type = models.ForeignKey(
        FeeType,
        on_delete=models.CASCADE,
        related_name='fee_structures'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(
        max_length=20,
        choices=FeeFrequency.choices,
        default=FeeFrequency.MONTHLY
    )
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        related_name='fee_structures'
    )
    due_day = models.IntegerField(default=10, help_text="Day of month when fee is due")
    late_fee_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    late_fee_after_days = models.IntegerField(default=5)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'fee_structures'
        verbose_name = _('Fee Structure')
        verbose_name_plural = _('Fee Structures')
        unique_together = ['class_name', 'fee_type', 'academic_year']
    
    def __str__(self):
        return f"{self.class_name.name} - {self.fee_type.name} - {self.amount}"


class FeeInvoice(models.Model):
    """Fee Invoices for Students"""
    
    class InvoiceStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        PARTIAL = 'PARTIAL', _('Partially Paid')
        PAID = 'PAID', _('Paid')
        OVERDUE = 'OVERDUE', _('Overdue')
        CANCELLED = 'CANCELLED', _('Cancelled')
    
    invoice_number = models.CharField(max_length=50, unique=True)
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='fee_invoices'
    )
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        related_name='fee_invoices'
    )
    invoice_date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(
        max_length=20,
        choices=InvoiceStatus.choices,
        default=InvoiceStatus.PENDING
    )
    remarks = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_invoices'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'fee_invoices'
        verbose_name = _('Fee Invoice')
        verbose_name_plural = _('Fee Invoices')
        ordering = ['-invoice_date']
    
    def __str__(self):
        return f"{self.invoice_number} - {self.student.admission_number}"
    
    @property
    def balance_amount(self):
        return self.total_amount + self.late_fee - self.discount_amount - self.paid_amount
    
    def update_status(self):
        balance = self.balance_amount
        if balance <= 0:
            self.status = self.InvoiceStatus.PAID
        elif self.paid_amount > 0:
            self.status = self.InvoiceStatus.PARTIAL
        elif self.due_date < models.DateField().today():
            self.status = self.InvoiceStatus.OVERDUE
        else:
            self.status = self.InvoiceStatus.PENDING
        self.save()


class FeeInvoiceItem(models.Model):
    """Individual Items in Fee Invoice"""
    invoice = models.ForeignKey(
        FeeInvoice,
        on_delete=models.CASCADE,
        related_name='items'
    )
    fee_type = models.ForeignKey(
        FeeType,
        on_delete=models.CASCADE,
        related_name='invoice_items'
    )
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'fee_invoice_items'
        verbose_name = _('Fee Invoice Item')
        verbose_name_plural = _('Fee Invoice Items')
    
    def __str__(self):
        return f"{self.invoice.invoice_number} - {self.fee_type.name}"


class Payment(models.Model):
    """Payment Records"""
    
    class PaymentMethod(models.TextChoices):
        CASH = 'CASH', _('Cash')
        CHEQUE = 'CHEQUE', _('Cheque')
        BANK_TRANSFER = 'BANK_TRANSFER', _('Bank Transfer')
        ONLINE = 'ONLINE', _('Online Payment')
        CARD = 'CARD', _('Credit/Debit Card')
    
    class PaymentStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        COMPLETED = 'COMPLETED', _('Completed')
        FAILED = 'FAILED', _('Failed')
        REFUNDED = 'REFUNDED', _('Refunded')
    
    receipt_number = models.CharField(max_length=50, unique=True)
    invoice = models.ForeignKey(
        FeeInvoice,
        on_delete=models.CASCADE,
        related_name='payments'
    )
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,
        default=PaymentMethod.CASH
    )
    payment_status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.COMPLETED
    )
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    cheque_number = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    received_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='received_payments'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'payments'
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')
        ordering = ['-payment_date']
    
    def __str__(self):
        return f"{self.receipt_number} - {self.amount}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update invoice paid amount
        if self.payment_status == self.PaymentStatus.COMPLETED:
            invoice = self.invoice
            invoice.paid_amount = invoice.payments.filter(
                payment_status=self.PaymentStatus.COMPLETED
            ).aggregate(total=models.Sum('amount'))['total'] or Decimal('0.00')
            invoice.update_status()


class Discount(models.Model):
    """Discount Management"""
    
    class DiscountType(models.TextChoices):
        PERCENTAGE = 'PERCENTAGE', _('Percentage')
        FIXED = 'FIXED', _('Fixed Amount')
    
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    discount_type = models.CharField(
        max_length=20,
        choices=DiscountType.choices,
        default=DiscountType.PERCENTAGE
    )
    value = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'discounts'
        verbose_name = _('Discount')
        verbose_name_plural = _('Discounts')
    
    def __str__(self):
        return f"{self.name} ({self.value}{'%' if self.discount_type == 'PERCENTAGE' else ''})"


class StudentDiscount(models.Model):
    """Discount Applied to Students"""
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='discounts'
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.CASCADE,
        related_name='student_discounts'
    )
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        related_name='student_discounts'
    )
    reason = models.TextField(blank=True, null=True)
    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='approved_discounts'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'student_discounts'
        verbose_name = _('Student Discount')
        verbose_name_plural = _('Student Discounts')
    
    def __str__(self):
        return f"{self.student.admission_number} - {self.discount.name}"


class Expense(models.Model):
    """Expense Management"""
    
    class ExpenseCategory(models.TextChoices):
        SALARY = 'SALARY', _('Salary')
        UTILITY = 'UTILITY', _('Utility Bills')
        MAINTENANCE = 'MAINTENANCE', _('Maintenance')
        STATIONERY = 'STATIONERY', _('Stationery')
        TRANSPORT = 'TRANSPORT', _('Transport')
        FOOD = 'FOOD', _('Food')
        OTHER = 'OTHER', _('Other')
    
    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=20,
        choices=ExpenseCategory.choices
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    receipt = models.FileField(upload_to='expense_receipts/', blank=True, null=True)
    paid_to = models.CharField(max_length=200, blank=True, null=True)
    payment_method = models.CharField(
        max_length=20,
        choices=Payment.PaymentMethod.choices,
        default=Payment.PaymentMethod.CASH
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_expenses'
    )
    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_expenses'
    )
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'expenses'
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.title} - {self.amount}"


class Salary(models.Model):
    """Staff Salary Management"""
    
    class SalaryStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        PAID = 'PAID', _('Paid')
        CANCELLED = 'CANCELLED', _('Cancelled')
    
    staff = models.ForeignKey(
        'staff.Staff',
        on_delete=models.CASCADE,
        related_name='salaries'
    )
    month = models.IntegerField()
    year = models.IntegerField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(null=True, blank=True)
    payment_method = models.CharField(
        max_length=20,
        choices=Payment.PaymentMethod.choices,
        default=Payment.PaymentMethod.BANK_TRANSFER
    )
    status = models.CharField(
        max_length=20,
        choices=SalaryStatus.choices,
        default=SalaryStatus.PENDING
    )
    remarks = models.TextField(blank=True, null=True)
    processed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='processed_salaries'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'salaries'
        verbose_name = _('Salary')
        verbose_name_plural = _('Salaries')
        unique_together = ['staff', 'month', 'year']
        ordering = ['-year', '-month']
    
    def __str__(self):
        return f"{self.staff.user.get_full_name()} - {self.month}/{self.year}"
    
    def save(self, *args, **kwargs):
        self.net_salary = self.basic_salary + self.allowances + self.bonus - self.deductions
        super().save(*args, **kwargs)
