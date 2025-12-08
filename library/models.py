from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User, Campus


class BookCategory(models.Model):
    """Book Category Management"""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'book_categories'
        verbose_name = _('Book Category')
        verbose_name_plural = _('Book Categories')
    
    def __str__(self):
        return self.name


class Book(models.Model):
    """Book Management"""
    title = models.CharField(max_length=300)
    isbn = models.CharField(max_length=20, unique=True, blank=True, null=True)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(
        BookCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
        related_name='library_books'
    )
    total_copies = models.IntegerField(default=1)
    available_copies = models.IntegerField(default=1)
    rack_number = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'books'
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class BookIssue(models.Model):
    """Book Issue/Return Management"""
    
    class IssueStatus(models.TextChoices):
        ISSUED = 'ISSUED', _('Issued')
        RETURNED = 'RETURNED', _('Returned')
        LOST = 'LOST', _('Lost')
        DAMAGED = 'DAMAGED', _('Damaged')
    
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='issues'
    )
    issued_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='issued_books'
    )
    issue_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=IssueStatus.choices,
        default=IssueStatus.ISSUED
    )
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fine_paid = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)
    issued_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='issued_books_as_librarian'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'book_issues'
        verbose_name = _('Book Issue')
        verbose_name_plural = _('Book Issues')
        ordering = ['-issue_date']
    
    def __str__(self):
        return f"{self.book.title} - {self.issued_to.get_full_name()}"
    
    def save(self, *args, **kwargs):
        # Update available copies
        if self.pk is None:  # New issue
            self.book.available_copies -= 1
            self.book.save()
        else:  # Returning book
            old_status = BookIssue.objects.get(pk=self.pk).status
            if old_status == self.IssueStatus.ISSUED and self.status == self.IssueStatus.RETURNED:
                self.book.available_copies += 1
                self.book.save()
        super().save(*args, **kwargs)
