import csv
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import Student
from .forms import StudentReportFilterForm

@login_required
def index(request):
    """Reports Dashboard"""
    return render(request, 'reports/index.html')

@login_required
def student_report(request):
    """Student detailed report with filtering and export"""
    form = StudentReportFilterForm(request.GET)
    students = Student.objects.select_related('user', 'current_class', 'section', 'campus').all().order_by('current_class__numeric_value', 'user__first_name')
    
    if form.is_valid():
        if form.cleaned_data['class_group']:
            students = students.filter(current_class=form.cleaned_data['class_group'])
        if form.cleaned_data['section']:
            students = students.filter(section=form.cleaned_data['section'])
        if form.cleaned_data['gender']:
            students = students.filter(user__gender=form.cleaned_data['gender'])
        if form.cleaned_data['status']:
            students = students.filter(status=form.cleaned_data['status'])
            
    # Check for export
    if request.GET.get('export') == 'csv':
        return export_student_csv(students)
        
    context = {
        'form': form,
        'students': students,
    }
    return render(request, 'reports/student_report.html', context)

def export_student_csv(queryset):
    """Helper to export student queryset to CSV"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="student_report_{timestamp}.csv"'
    
    writer = csv.writer(response)
    writer.writerow([
        'Admission No', 'First Name', 'Last Name', 'Gender', 
        'Date of Birth', 'Class', 'Section', 'Roll No',
        'Father Name', 'Father Phone', 'Mother Name', 
        'Address', 'Status', 'Admission Date'
    ])
    
    for student in queryset:
        writer.writerow([
            student.admission_number,
            student.user.first_name,
            student.user.last_name,
            student.user.get_gender_display(),
            student.user.date_of_birth,
            student.current_class.name if student.current_class else '-',
            student.section.name if student.section else '-',
            student.roll_number,
            student.father_name,
            student.father_phone,
            student.mother_name,
            student.user.address,
            student.get_status_display(),
            student.admission_date
        ])
        
    return response
