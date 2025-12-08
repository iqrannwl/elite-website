from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Sum, Q
from django.utils import timezone
from datetime import datetime, timedelta

from students.models import Student
from academics.models import Class, Attendance, Examination
from staff.models import Staff, Leave
from communication.models import Announcement
from finance.models import FeeInvoice


@login_required
def dashboard(request):
    """Main dashboard view"""
    context = {
        'total_students': Student.objects.filter(status='ACTIVE').count(),
        'total_teachers': Staff.objects.filter(
            user__role='TEACHER',
            is_active=True
        ).count(),
        'total_classes': Class.objects.filter(is_active=True).count(),
        'pending_fees': FeeInvoice.objects.filter(
            status__in=['PENDING', 'PARTIAL', 'OVERDUE']
        ).aggregate(
            total=Sum('total_amount')
        )['total'] or 0,
        
        # Today's attendance
        'present_today': Attendance.objects.filter(
            date=timezone.now().date(),
            status='PRESENT'
        ).count(),
        'absent_today': Attendance.objects.filter(
            date=timezone.now().date(),
            status='ABSENT'
        ).count(),
        
        # Staff on leave
        'staff_on_leave': Leave.objects.filter(
            start_date__lte=timezone.now().date(),
            end_date__gte=timezone.now().date(),
            status='APPROVED'
        ).count(),
        
        # Upcoming exams
        'upcoming_exams': Examination.objects.filter(
            start_date__gte=timezone.now().date(),
            start_date__lte=timezone.now().date() + timedelta(days=30)
        ).count(),
        
        # Recent data
        'recent_students': Student.objects.filter(
            status='ACTIVE'
        ).select_related('user', 'current_class').order_by('-admission_date')[:5],
        
        'recent_announcements': Announcement.objects.filter(
            is_active=True,
            start_date__lte=timezone.now().date(),
            end_date__gte=timezone.now().date()
        ).order_by('-created_at')[:5],
        
        'upcoming_events': [],  # Add events model later
    }
    
    return render(request, 'school/dashboard.html', context)


@login_required
def students_list(request):
    """List all students"""
    students = Student.objects.filter(
        status='ACTIVE'
    ).select_related('user', 'current_class', 'section', 'campus')
    
    # Filter by class if provided
    class_filter = request.GET.get('class')
    if class_filter:
        students = students.filter(current_class_id=class_filter)
    
    # Search
    search = request.GET.get('search')
    if search:
        students = students.filter(
            Q(admission_number__icontains=search) |
            Q(user__first_name__icontains=search) |
            Q(user__last_name__icontains=search)
        )
    
    context = {
        'students': students,
        'classes': Class.objects.filter(is_active=True),
    }
    
    return render(request, 'school/students/list.html', context)


@login_required
def student_add(request):
    """Add new student"""
    from students.forms import StudentForm
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.user.get_full_name()} added successfully!')
            return redirect('school:student_detail', pk=student.pk)
    else:
        form = StudentForm()
    
    context = {
        'form': form,
    }
    return render(request, 'school/students/form.html', context)


@login_required
def student_edit(request, pk):
    """Edit student"""
    from students.forms import StudentForm
    
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.user.get_full_name()} updated successfully!')
            return redirect('school:student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    
    context = {
        'form': form,
    }
    return render(request, 'school/students/form.html', context)


@login_required
def student_detail(request, pk):
    """Student detail view"""
    student = get_object_or_404(
        Student.objects.select_related('user', 'current_class', 'section'),
        pk=pk
    )
    
    context = {
        'student': student,
        'documents': student.documents.all(),
        'health_records': student.health_records.all()[:5],
        'attendance_stats': Attendance.objects.filter(
            student=student
        ).values('status').annotate(count=Count('id')),
    }
    
    return render(request, 'school/students/detail.html', context)


@login_required
def staff_list(request):
    """List all staff"""
    staff = Staff.objects.filter(
        is_active=True
    ).select_related('user', 'department', 'designation', 'campus')
    
    context = {
        'staff': staff,
    }
    
    return render(request, 'school/staff/list.html', context)


@login_required
def academics_view(request):
    """Academics overview"""
    context = {
        'classes': Class.objects.filter(is_active=True).prefetch_related('sections'),
    }
    
    return render(request, 'school/academics/index.html', context)


@login_required
def attendance_view(request):
    """Attendance management"""
    today = timezone.now().date()
    
    context = {
        'today': today,
        'attendance_records': Attendance.objects.filter(
            date=today
        ).select_related('student__user'),
    }
    
    return render(request, 'school/attendance/index.html', context)


@login_required
def exams_view(request):
    """Examinations view"""
    context = {
        'upcoming_exams': Examination.objects.filter(
            start_date__gte=timezone.now().date()
        ).order_by('start_date'),
        'past_exams': Examination.objects.filter(
            end_date__lt=timezone.now().date()
        ).order_by('-start_date')[:10],
    }
    
    return render(request, 'school/exams/index.html', context)


@login_required
def finance_view(request):
    """Finance overview"""
    context = {
        'total_revenue': FeeInvoice.objects.filter(
            status='PAID'
        ).aggregate(total=Sum('total_amount'))['total'] or 0,
        'pending_amount': FeeInvoice.objects.filter(
            status__in=['PENDING', 'PARTIAL', 'OVERDUE']
        ).aggregate(total=Sum('total_amount'))['total'] or 0,
        'recent_invoices': FeeInvoice.objects.select_related(
            'student__user'
        ).order_by('-invoice_date')[:10],
    }
    
    return render(request, 'school/finance/index.html', context)


@login_required
def library_view(request):
    """Library view"""
    return render(request, 'school/library/index.html')


@login_required
def transport_view(request):
    """Transport view"""
    return render(request, 'school/transport/index.html')


@login_required
def hostel_view(request):
    """Hostel view"""
    return render(request, 'school/hostel/index.html')


@login_required
def communication_view(request):
    """Communication view"""
    context = {
        'announcements': Announcement.objects.filter(
            is_active=True
        ).order_by('-created_at'),
    }
    
    return render(request, 'school/communication/index.html', context)


@login_required
def reports_view(request):
    """Reports view"""
    return render(request, 'school/reports/index.html')


@login_required
def settings_view(request):
    """Settings view"""
    return render(request, 'school/settings/index.html')
