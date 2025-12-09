# 🚀 Quick Start Guide - Using Form Templates

## How to Use the Form Templates

All form templates are ready to use! Here's a quick guide to integrate them into your Django views.

---

## 📝 Step-by-Step Integration

### Step 1: Ensure Forms Exist

Make sure you have the corresponding Django forms in your apps. For example:

```python
# students/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'admission_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            # ... add widgets for all fields
        }
```

### Step 2: Create Views

Create views in your app's `views.py`:

```python
# students/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentForm

def student_create(request):
    """Create new student"""
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.first_name} added successfully!')
            return redirect('students:student_list')
    else:
        form = StudentForm()
    
    return render(request, 'school/students/student_form.html', {
        'form': form
    })

def student_edit(request, pk):
    """Edit existing student"""
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student {student.first_name} updated successfully!')
            return redirect('students:student_list')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'school/students/student_form.html', {
        'form': form
    })
```

### Step 3: Add URL Patterns

Add URLs in your app's `urls.py`:

```python
# students/urls.py
from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.student_create, name='student_create'),
    path('<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),
]
```

### Step 4: Include in Main URLs

Include app URLs in main `urls.py`:

```python
# elite_website/urls.py
from django.urls import path, include

urlpatterns = [
    # ... other patterns
    path('school/students/', include('students.urls')),
    path('school/staff/', include('staff.urls')),
    path('school/academics/', include('academics.urls')),
    path('school/finance/', include('finance.urls')),
    path('school/library/', include('library.urls')),
    path('school/transport/', include('transport.urls')),
    path('school/hostel/', include('hostel.urls')),
    path('school/communication/', include('communication.urls')),
]
```

---

## 📋 Complete Example: Staff Module

### 1. Form (staff/forms.py)

```python
from django import forms
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = [
            'first_name', 'last_name', 'email', 'phone',
            'date_of_birth', 'gender', 'address',
            'employee_id', 'department', 'designation',
            'date_of_joining', 'qualification', 'experience_years',
            'basic_salary', 'contract_type',
            'bank_name', 'account_number', 'is_active'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_joining': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control'}),
            'experience_years': forms.NumberInput(attrs={'class': 'form-control'}),
            'basic_salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'contract_type': forms.Select(attrs={'class': 'form-select'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'account_number': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
```

### 2. Views (staff/views.py)

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Staff
from .forms import StaffForm

@login_required
def staff_list(request):
    """List all staff members"""
    staff_members = Staff.objects.all().order_by('-created_at')
    return render(request, 'school/staff/list.html', {
        'staff_members': staff_members
    })

@login_required
def staff_create(request):
    """Create new staff member"""
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            staff = form.save()
            messages.success(request, f'Staff member {staff.first_name} {staff.last_name} added successfully!')
            return redirect('staff:staff_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StaffForm()
    
    return render(request, 'school/staff/staff_form.html', {
        'form': form
    })

@login_required
def staff_edit(request, pk):
    """Edit existing staff member"""
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, f'Staff member {staff.first_name} {staff.last_name} updated successfully!')
            return redirect('staff:staff_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StaffForm(instance=staff)
    
    return render(request, 'school/staff/staff_form.html', {
        'form': form
    })

@login_required
def staff_delete(request, pk):
    """Delete staff member"""
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        name = f'{staff.first_name} {staff.last_name}'
        staff.delete()
        messages.success(request, f'Staff member {name} deleted successfully!')
        return redirect('staff:staff_list')
    
    return render(request, 'school/staff/confirm_delete.html', {
        'staff': staff
    })
```

### 3. URLs (staff/urls.py)

```python
from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.staff_list, name='staff_list'),
    path('add/', views.staff_create, name='staff_create'),
    path('<int:pk>/edit/', views.staff_edit, name='staff_edit'),
    path('<int:pk>/delete/', views.staff_delete, name='staff_delete'),
]
```

---

## 🎯 Template Usage Patterns

### Pattern 1: Simple Form (Generic Template)

For simple models like Campus, Holiday, etc., use the generic template:

```python
def campus_create(request):
    if request.method == 'POST':
        form = CampusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:campus_list')
    else:
        form = CampusForm()
    
    return render(request, 'school/generic_form.html', {
        'form': form,
        'title': 'Campus',
        'icon': 'building',
        'back_url': 'accounts:campus_list'
    })
```

### Pattern 2: Complex Form (Custom Template)

For complex models like Student, Staff, use custom templates:

```python
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students:student_list')
    else:
        form = StudentForm()
    
    return render(request, 'school/students/student_form.html', {
        'form': form
    })
```

---

## 🔧 Customization Tips

### Adding Custom Context

```python
def student_create(request):
    form = StudentForm()
    
    return render(request, 'school/students/student_form.html', {
        'form': form,
        'classes': Class.objects.filter(is_active=True),
        'academic_years': AcademicYear.objects.all(),
    })
```

### Adding AJAX Functionality

```javascript
// In your template
<script>
document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    
    fetch(this.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = data.redirect_url;
        }
    });
});
</script>
```

---

## ✅ Checklist for Each Module

- [ ] Create Django form in `forms.py`
- [ ] Add form widgets with Bootstrap classes
- [ ] Create list view
- [ ] Create create view
- [ ] Create edit view
- [ ] Create delete view
- [ ] Add URL patterns
- [ ] Test form validation
- [ ] Test create operation
- [ ] Test edit operation
- [ ] Test delete operation

---

## 🎨 Form Widget Classes Reference

```python
# Text inputs
forms.TextInput(attrs={'class': 'form-control'})

# Email
forms.EmailInput(attrs={'class': 'form-control'})

# Number
forms.NumberInput(attrs={'class': 'form-control'})

# Date
forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})

# Textarea
forms.Textarea(attrs={'class': 'form-control', 'rows': 3})

# Select
forms.Select(attrs={'class': 'form-select'})

# Checkbox
forms.CheckboxInput(attrs={'class': 'form-check-input'})

# File
forms.FileInput(attrs={'class': 'form-control'})
```

---

## 🚀 Ready to Go!

All templates are created and ready to use. Just follow the patterns above for each module, and you'll have a fully functional school management system!

**Happy Coding! 🎉**
