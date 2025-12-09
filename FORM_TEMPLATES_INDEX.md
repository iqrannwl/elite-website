# 📑 Form Templates Index

## Quick Reference Guide

| Module | Template File | Purpose | URL Name |
|--------|--------------|---------|----------|
| **Students** | `students/student_form.html` | Add/Edit Student | `students:student_create` / `students:student_edit` |
| **Staff** | `staff/staff_form.html` | Add/Edit Staff | `staff:staff_create` / `staff:staff_edit` |
| **Classes** | `academics/class_form.html` | Add/Edit Class | `academics:class_create` / `academics:class_edit` |
| **Sections** | `academics/section_form.html` | Add/Edit Section | `academics:section_create` / `academics:section_edit` |
| **Subjects** | `academics/subject_form.html` | Add/Edit Subject | `academics:subject_create` / `academics:subject_edit` |
| **Attendance** | `attendance/attendance_form.html` | Mark Attendance | `academics:attendance_mark` |
| **Exams** | `exams/exam_form.html` | Create/Edit Exam | `academics:exam_create` / `academics:exam_edit` |
| **Fee Structure** | `finance/fee_structure_form.html` | Setup Fee Structure | `finance:fee_structure_create` / `finance:fee_structure_edit` |
| **Invoice** | `finance/invoice_form.html` | Generate Invoice | `finance:invoice_create` / `finance:invoice_edit` |
| **Payment** | `finance/payment_form.html` | Record Payment | `finance:payment_create` / `finance:payment_edit` |
| **Books** | `library/book_form.html` | Add/Edit Book | `library:book_create` / `library:book_edit` |
| **Book Issue** | `library/book_issue_form.html` | Issue/Return Book | `library:book_issue` |
| **Vehicles** | `transport/vehicle_form.html` | Add/Edit Vehicle | `transport:vehicle_create` / `transport:vehicle_edit` |
| **Routes** | `transport/route_form.html` | Add/Edit Route | `transport:route_create` / `transport:route_edit` |
| **Hostels** | `hostel/hostel_form.html` | Add/Edit Hostel | `hostel:hostel_create` / `hostel:hostel_edit` |
| **Announcements** | `communication/announcement_form.html` | Create Announcement | `communication:announcement_create` / `communication:announcement_edit` |
| **Generic** | `generic_form.html` | Any Simple Form | Reusable |

## 📊 Total Count

- **Total Templates**: 17
- **Modules Covered**: 9
- **Status**: ✅ All Complete

## 🎨 Template Features

All templates include:
- ✅ Bootstrap 5 styling
- ✅ Responsive design
- ✅ Error handling
- ✅ Form validation
- ✅ CSRF protection
- ✅ Back navigation
- ✅ Icons
- ✅ Help text

## 📁 File Locations

```
templates/school/
├── students/student_form.html
├── staff/staff_form.html
├── academics/
│   ├── class_form.html
│   ├── section_form.html
│   └── subject_form.html
├── attendance/attendance_form.html
├── exams/exam_form.html
├── finance/
│   ├── fee_structure_form.html
│   ├── invoice_form.html
│   └── payment_form.html
├── library/
│   ├── book_form.html
│   └── book_issue_form.html
├── transport/
│   ├── vehicle_form.html
│   └── route_form.html
├── hostel/hostel_form.html
├── communication/announcement_form.html
└── generic_form.html
```

## 🚀 Usage

1. Create corresponding Django form
2. Create view function
3. Add URL pattern
4. Template is ready to use!

See `FORM_TEMPLATES_QUICK_START.md` for detailed examples.
