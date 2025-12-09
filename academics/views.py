from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Class, Section, Subject, Attendance, Examination
from .forms import ClassForm, SectionForm, SubjectForm, AttendanceForm, ExaminationForm


# ==================== CLASS VIEWS ====================

@login_required
def class_list(request):
    """List all classes"""
    classes_list = Class.objects.all().order_by('numeric_value')
    paginator = Paginator(classes_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'school/academics/index.html', {
        'classes': page_obj
    })




@login_required
def class_create(request):
    """Create new class"""
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            class_obj = form.save()
            messages.success(request, f'Class {class_obj.name} created successfully!')
            return redirect('academics:class_list')
    else:
        form = ClassForm()
    
    return render(request, 'school/academics/class_form.html', {
        'form': form
    })


@login_required
def class_edit(request, pk):
    """Edit existing class"""
    class_obj = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=class_obj)
        if form.is_valid():
            form.save()
            messages.success(request, f'Class {class_obj.name} updated successfully!')
            return redirect('academics:class_list')
    else:
        form = ClassForm(instance=class_obj)
    
    return render(request, 'school/academics/class_form.html', {
        'form': form
    })


@login_required
def class_delete(request, pk):
    """Delete class"""
    class_obj = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        name = class_obj.name
        class_obj.delete()
        messages.success(request, f'Class {name} deleted successfully!')
        return redirect('academics:class_list')
    
    return render(request, 'school/academics/class_confirm_delete.html', {
        'class': class_obj
    })


# ==================== SECTION VIEWS ====================

@login_required
def section_list(request):
    """List all sections"""
    sections_list = Section.objects.all().select_related('class_name')
    paginator = Paginator(sections_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'school/academics/index.html', {
        'sections': page_obj
    })


@login_required
def section_create(request):
    """Create new section"""
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save()
            messages.success(request, f'Section {section.name} created successfully!')
            return redirect('academics:section_list')
    else:
        form = SectionForm()
        # Pre-fill class if provided in query params
        if 'class' in request.GET:
            form.initial['class_name'] = request.GET.get('class')
    
    return render(request, 'school/academics/section_form.html', {
        'form': form
    })


@login_required
def section_edit(request, pk):
    """Edit existing section"""
    section = get_object_or_404(Section, pk=pk)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            messages.success(request, f'Section {section.name} updated successfully!')
            return redirect('academics:section_list')
    else:
        form = SectionForm(instance=section)
    
    return render(request, 'school/academics/section_form.html', {
        'form': form
    })


@login_required
def section_delete(request, pk):
    """Delete section"""
    section = get_object_or_404(Section, pk=pk)
    if request.method == 'POST':
        name = section.name
        section.delete()
        messages.success(request, f'Section {name} deleted successfully!')
        return redirect('academics:section_list')
    
    return render(request, 'school/academics/section_confirm_delete.html', {
        'section': section
    })


# ==================== SUBJECT VIEWS ====================

@login_required
def subject_list(request):
    """List all subjects"""
    subjects_list = Subject.objects.all().select_related('teacher')
    paginator = Paginator(subjects_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'school/academics/index.html', {
        'subjects': page_obj
    })


@login_required
def subject_create(request):
    """Create new subject"""
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save()
            messages.success(request, f'Subject {subject.name} created successfully!')
            return redirect('academics:subject_list')
    else:
        form = SubjectForm()
    
    return render(request, 'school/academics/subject_form.html', {
        'form': form
    })


@login_required
def subject_edit(request, pk):
    """Edit existing subject"""
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, f'Subject {subject.name} updated successfully!')
            return redirect('academics:subject_list')
    else:
        form = SubjectForm(instance=subject)
    
    return render(request, 'school/academics/subject_form.html', {
        'form': form
    })


@login_required
def subject_delete(request, pk):
    """Delete subject"""
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        name = subject.name
        subject.delete()
        messages.success(request, f'Subject {name} deleted successfully!')
        return redirect('academics:subject_list')
    
    return render(request, 'school/academics/subject_confirm_delete.html', {
        'subject': subject
    })


# ==================== ATTENDANCE VIEWS ====================

@login_required
def attendance_list(request):
    """List all attendance records"""
    attendance_qs = Attendance.objects.all().select_related('student', 'class_name').order_by('-date')
    paginator = Paginator(attendance_qs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'school/attendance/index.html', {
        'attendance_records': page_obj
    })


@login_required
def attendance_mark(request):
    """Mark attendance"""
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance marked successfully!')
            return redirect('academics:attendance_list')
    else:
        form = AttendanceForm()
    
    return render(request, 'school/attendance/attendance_form.html', {
        'form': form
    })


@login_required
def attendance_edit(request, pk):
    """Edit attendance record"""
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance updated successfully!')
            return redirect('academics:attendance_list')
    else:
        form = AttendanceForm(instance=attendance)
    
    return render(request, 'school/attendance/attendance_form.html', {
        'form': form
    })


# ==================== EXAM VIEWS ====================

@login_required
def exam_list(request):
    """List all exams"""
    exams_qs = Examination.objects.all().select_related('class_name', 'subject').order_by('-exam_date')
    paginator = Paginator(exams_qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'school/exams/index.html', {
        'exams': page_obj
    })


@login_required
def exam_create(request):
    """Create new exam"""
    if request.method == 'POST':
        form = ExaminationForm(request.POST)
        if form.is_valid():
            exam = form.save()
            messages.success(request, f'Exam {exam.name} created successfully!')
            return redirect('academics:exam_list')
    else:
        form = ExaminationForm()
    
    return render(request, 'school/exams/exam_form.html', {
        'form': form
    })


@login_required
def exam_edit(request, pk):
    """Edit existing exam"""
    exam = get_object_or_404(Examination, pk=pk)
    if request.method == 'POST':
        form = ExaminationForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            messages.success(request, f'Exam {exam.name} updated successfully!')
            return redirect('academics:exam_list')
    else:
        form = ExaminationForm(instance=exam)
    
    return render(request, 'school/exams/exam_form.html', {
        'form': form
    })


@login_required
def exam_delete(request, pk):
    """Delete exam"""
    exam = get_object_or_404(Examination, pk=pk)
    if request.method == 'POST':
        name = exam.name
        exam.delete()
        messages.success(request, f'Exam {name} deleted successfully!')
        return redirect('academics:exam_list')
    
    return render(request, 'school/exams/exam_confirm_delete.html', {
        'exam': exam
    })
