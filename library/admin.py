from django.contrib import admin
from .models import BookCategory, Book, BookIssue


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'code')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'isbn', 'category', 'campus',
        'total_copies', 'available_copies', 'is_active'
    )
    list_filter = ('category', 'campus', 'is_active')
    search_fields = ('title', 'author', 'isbn')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(BookIssue)
class BookIssueAdmin(admin.ModelAdmin):
    list_display = (
        'book', 'issued_to', 'issue_date', 'due_date',
        'return_date', 'status', 'fine_amount', 'fine_paid'
    )
    list_filter = ('status', 'fine_paid', 'issue_date')
    search_fields = ('book__title', 'issued_to__first_name', 'issued_to__last_name')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'issue_date'
