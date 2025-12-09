# 🔄 Admin Links Removal - Batch Update Script

## Templates Updated

### ✅ Completed
1. **templates/school/staff/list.html**
   - `admin:staff_staff_add` → `staff:staff_create`
   - `admin:staff_staff_change` → `staff:staff_edit`

2. **templates/school/academics/index.html**
   - `admin:academics_class_add` → `academics:class_create`
   - `admin:academics_class_change` → `academics:class_edit`
   - `admin:academics_section_add` → `academics:section_create`

## 📋 Remaining Templates to Update

### High Priority

#### 1. Attendance Module
**File**: `templates/school/attendance/index.html`
```
FIND: {% url 'admin:academics_attendance_add' %}
REPLACE: {% url 'academics:attendance_mark' %}
```

#### 2. Exams Module
**File**: `templates/school/exams/index.html`
```
FIND: {% url 'admin:academics_examination_add' %}
REPLACE: {% url 'academics:exam_create' %}

FIND: {% url 'admin:academics_examination_change' exam.pk %}
REPLACE: {% url 'academics:exam_edit' exam.pk %}

FIND: {% url 'admin:academics_examschedule_add' %}
REPLACE: {% url 'academics:exam_schedule_create' %}
```

#### 3. Finance Module
**File**: `templates/school/finance/index.html`
```
FIND: {% url 'admin:finance_feeinvoice_add' %}
REPLACE: {% url 'finance:invoice_create' %}

FIND: {% url 'admin:finance_feeinvoice_change' invoice.pk %}
REPLACE: {% url 'finance:invoice_edit' invoice.pk %}

FIND: {% url 'admin:finance_payment_add' %}
REPLACE: {% url 'finance:payment_create' %}
```

#### 4. Communication Module
**File**: `templates/school/communication/index.html`
```
FIND: {% url 'admin:communication_announcement_add' %}
REPLACE: {% url 'communication:announcement_create' %}
```

#### 5. Library Module
**File**: `templates/school/library/index.html`
```
FIND: {% url 'admin:library_book_add' %}
REPLACE: {% url 'library:book_create' %}

UPDATE TEXT: "Add books via admin panel" → "Add books using the form"
```

#### 6. Transport Module
**File**: `templates/school/transport/index.html`
```
FIND: {% url 'admin:transport_vehicle_add' %}
REPLACE: {% url 'transport:vehicle_create' %}

UPDATE TEXT: "Manage vehicles and routes via admin panel" → "Manage vehicles and routes"
```

#### 7. Hostel Module
**File**: `templates/school/hostel/index.html`
```
FIND: {% url 'admin:hostel_hostel_add' %}
REPLACE: {% url 'hostel:hostel_create' %}

UPDATE TEXT: "Manage hostels and rooms via admin panel" → "Manage hostels and rooms"
```

### Medium Priority

#### 8. Settings Module
**File**: `templates/school/settings/index.html`

Multiple admin links - needs comprehensive update:
```
Campus: admin:accounts_campus_changelist → accounts:campus_list
Academic Year: admin:accounts_academicyear_changelist → accounts:academic_year_list
Holiday: admin:accounts_holiday_changelist → accounts:holiday_list
Classes: admin:academics_class_changelist → academics:class_list
Subjects: admin:academics_subject_changelist → academics:subject_list
Fee Types: admin:finance_feetype_changelist → finance:fee_type_list
Fee Structure: admin:finance_feestructure_changelist → finance:fee_structure_list
Users: admin:accounts_user_changelist → accounts:user_list
Departments: admin:staff_department_changelist → staff:department_list
Designations: admin:staff_designation_changelist → staff:designation_list
```

#### 9. Reports Module
**File**: `templates/school/reports/index.html`

Multiple admin links for reports:
```
Students: admin:students_student_changelist → students:student_list
Finance: admin:finance_feeinvoice_changelist → finance:invoice_list
Exams: admin:academics_examination_changelist → academics:exam_list
Attendance: admin:academics_attendance_changelist → academics:attendance_list
Staff: admin:staff_staff_changelist → staff:staff_list
```

### Low Priority

#### 10. Navbar
**File**: `templates/navbar.html`
```
FIND: <a class="text-white" href="/admin" target="_blank">Login</a>
REPLACE: <a class="text-white" href="{% url 'accounts:login' %}">Login</a>
```

## 🎯 Summary

### Total Templates: 10
- ✅ **Completed**: 2 (Staff, Academics)
- 🔄 **In Progress**: 0
- ⏳ **Pending**: 8

### Total Admin Links: ~40+
- ✅ **Removed**: 6
- ⏳ **Remaining**: ~34

## 📝 Notes

1. All custom URLs need to be created in respective apps
2. Views need to be implemented for each URL
3. Forms are already created and ready to use
4. Templates for forms are already created

## 🚀 Next Steps

1. Update remaining high-priority templates
2. Create URL patterns in each app
3. Implement view functions
4. Test all forms
5. Update settings and reports (low priority)

---

**Last Updated**: December 9, 2025  
**Status**: 20% Complete
