from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import os

def create_documentation_pdf():
    """Create comprehensive PDF documentation for Elite School Management System"""
    
    # Create PDF
    pdf_filename = "Elite_School_Management_System_Documentation.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=A4,
                           rightMargin=72, leftMargin=72,
                           topMargin=72, bottomMargin=18)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#764ba2'),
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=8,
        alignment=TA_JUSTIFY
    )
    
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontSize=9,
        leftIndent=20,
        textColor=colors.HexColor('#333333'),
        backColor=colors.HexColor('#f5f5f5')
    )
    
    # Title Page
    elements.append(Spacer(1, 2*inch))
    elements.append(Paragraph("Elite School", title_style))
    elements.append(Paragraph("Management System", title_style))
    elements.append(Spacer(1, 0.5*inch))
    elements.append(Paragraph("Complete Documentation", heading1_style))
    elements.append(Spacer(1, 0.3*inch))
    elements.append(Paragraph(f"Generated: {datetime.now().strftime('%B %d, %Y')}", normal_style))
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("Version 1.0", normal_style))
    
    elements.append(PageBreak())
    
    # Table of Contents
    elements.append(Paragraph("Table of Contents", heading1_style))
    elements.append(Spacer(1, 0.2*inch))
    
    toc_data = [
        ["1.", "Introduction", "3"],
        ["2.", "System Overview", "4"],
        ["3.", "Installation Guide", "5"],
        ["4.", "User Roles & Permissions", "7"],
        ["5.", "Module Documentation", "8"],
        ["6.", "Database Models", "15"],
        ["7.", "API Reference", "18"],
        ["8.", "Troubleshooting", "20"],
    ]
    
    toc_table = Table(toc_data, colWidths=[0.5*inch, 4*inch, 1*inch])
    toc_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('ALIGN', (2, 0), (2, -1), 'RIGHT'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(toc_table)
    
    elements.append(PageBreak())
    
    # 1. Introduction
    elements.append(Paragraph("1. Introduction", heading1_style))
    elements.append(Paragraph(
        "Elite School Management System is a comprehensive web-based application designed to streamline "
        "and automate various administrative and academic processes in educational institutions. "
        "Built with Django 4.2.3 and modern web technologies, it provides a robust, scalable, and "
        "user-friendly platform for managing all aspects of school operations.",
        normal_style
    ))
    
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("Key Features:", heading2_style))
    
    features = [
        "Student Information Management",
        "Staff & Employee Management",
        "Academic Management (Classes, Subjects, Timetables)",
        "Attendance Tracking (Students & Staff)",
        "Examination & Grading System",
        "Fee Management & Financial Tracking",
        "Library Management",
        "Transport Management",
        "Hostel Management",
        "Communication System (Announcements, Messages)",
        "Comprehensive Reporting",
        "Role-Based Access Control"
    ]
    
    for feature in features:
        elements.append(Paragraph(f"• {feature}", normal_style))
    
    elements.append(PageBreak())
    
    # 2. System Overview
    elements.append(Paragraph("2. System Overview", heading1_style))
    
    elements.append(Paragraph("2.1 Technology Stack", heading2_style))
    tech_data = [
        ["Component", "Technology", "Version"],
        ["Backend Framework", "Django", "4.2.3"],
        ["Frontend", "HTML5, CSS3, JavaScript", "-"],
        ["UI Framework", "Bootstrap", "5.3.0"],
        ["Database", "SQLite / PostgreSQL", "-"],
        ["Icons", "Bootstrap Icons", "1.11.0"],
        ["Charts", "Chart.js", "Latest"],
        ["Python", "Python", "3.8+"],
    ]
    
    tech_table = Table(tech_data, colWidths=[2*inch, 2*inch, 1.5*inch])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
    ]))
    elements.append(tech_table)
    
    elements.append(Spacer(1, 0.3*inch))
    elements.append(Paragraph("2.2 System Architecture", heading2_style))
    elements.append(Paragraph(
        "The system follows a Model-View-Template (MVT) architecture pattern, which is Django's "
        "implementation of the MVC pattern. The application is divided into multiple Django apps, "
        "each handling a specific domain of the school management system.",
        normal_style
    ))
    
    elements.append(PageBreak())
    
    # 3. Installation Guide
    elements.append(Paragraph("3. Installation Guide", heading1_style))
    
    elements.append(Paragraph("3.1 Prerequisites", heading2_style))
    elements.append(Paragraph("• Python 3.8 or higher", normal_style))
    elements.append(Paragraph("• pip (Python package manager)", normal_style))
    elements.append(Paragraph("• Virtual environment (recommended)", normal_style))
    
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("3.2 Installation Steps", heading2_style))
    
    steps = [
        ("1. Clone the repository:", "git clone [repository-url]"),
        ("2. Create virtual environment:", "python -m venv .venv"),
        ("3. Activate virtual environment:", "source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate"),
        ("4. Install dependencies:", "pip install -r requirements.txt"),
        ("5. Run migrations:", "python manage.py migrate"),
        ("6. Create superuser:", "python manage.py createsuperuser"),
        ("7. Populate sample data:", "python manage.py populate_sample_data"),
        ("8. Run development server:", "python manage.py runserver"),
    ]
    
    for step, command in steps:
        elements.append(Paragraph(step, normal_style))
        elements.append(Paragraph(command, code_style))
        elements.append(Spacer(1, 0.1*inch))
    
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("3.3 Access Points", heading2_style))
    elements.append(Paragraph("• School Management: http://localhost:8000/school/", normal_style))
    elements.append(Paragraph("• Admin Panel: http://localhost:8000/admin/", normal_style))
    elements.append(Paragraph("• Login Page: http://localhost:8000/accounts/login/", normal_style))
    
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("3.4 Default Credentials", heading2_style))
    cred_data = [
        ["Role", "Username", "Password"],
        ["Admin", "admin", "admin123"],
        ["Staff", "staff1-staff10", "staff123"],
        ["Student", "student1-student30", "student123"],
    ]
    
    cred_table = Table(cred_data, colWidths=[1.5*inch, 2*inch, 2*inch])
    cred_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ]))
    elements.append(cred_table)
    
    elements.append(PageBreak())
    
    # 4. User Roles & Permissions
    elements.append(Paragraph("4. User Roles & Permissions", heading1_style))
    
    roles_data = [
        ["Role", "Description", "Key Permissions"],
        ["Super Admin", "Full system access", "All modules, settings, user management"],
        ["Admin", "School administrator", "Most modules except system settings"],
        ["Teacher", "Teaching staff", "Students, academics, attendance, exams"],
        ["Student", "Enrolled student", "View own records, assignments, grades"],
        ["Parent", "Student guardian", "View child's records, communicate"],
        ["Accountant", "Finance staff", "Fee management, invoices, payments"],
        ["Librarian", "Library staff", "Library management, book issues"],
        ["Receptionist", "Front desk", "Student admission, visitor management"],
    ]
    
    roles_table = Table(roles_data, colWidths=[1.3*inch, 2*inch, 2.2*inch])
    roles_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    elements.append(roles_table)
    
    elements.append(PageBreak())
    
    # 5. Module Documentation
    elements.append(Paragraph("5. Module Documentation", heading1_style))
    
    modules = [
        {
            "name": "5.1 Students Module",
            "description": "Comprehensive student information management system.",
            "features": [
                "Student registration and admission",
                "Personal and academic information",
                "Parent/Guardian details",
                "Health records and medical information",
                "Document management",
                "Student promotion and transfer",
                "Sibling management"
            ]
        },
        {
            "name": "5.2 Staff Module",
            "description": "Employee and staff management system.",
            "features": [
                "Staff registration and profiles",
                "Department and designation management",
                "Attendance tracking",
                "Leave management",
                "Salary and payroll",
                "Performance evaluation",
                "Document management"
            ]
        },
        {
            "name": "5.3 Academics Module",
            "description": "Academic operations and curriculum management.",
            "features": [
                "Class and section management",
                "Subject management",
                "Timetable creation",
                "Attendance marking",
                "Examination management",
                "Grade and result processing",
                "Homework assignments"
            ]
        },
        {
            "name": "5.4 Finance Module",
            "description": "Complete financial management system.",
            "features": [
                "Fee structure configuration",
                "Invoice generation",
                "Payment processing",
                "Discount management",
                "Expense tracking",
                "Salary management",
                "Financial reports"
            ]
        },
        {
            "name": "5.5 Library Module",
            "description": "Library resource management.",
            "features": [
                "Book cataloging",
                "Book issue and return",
                "Category management",
                "Member management",
                "Fine calculation",
                "Inventory tracking"
            ]
        },
        {
            "name": "5.6 Transport Module",
            "description": "School transport management.",
            "features": [
                "Vehicle management",
                "Route planning",
                "Stop management",
                "Driver information",
                "Maintenance tracking",
                "Student transport assignment"
            ]
        },
        {
            "name": "5.7 Hostel Module",
            "description": "Hostel and accommodation management.",
            "features": [
                "Hostel management",
                "Room allocation",
                "Facility management",
                "Complaint handling",
                "Warden assignment"
            ]
        },
        {
            "name": "5.8 Communication Module",
            "description": "Internal communication system.",
            "features": [
                "Announcements",
                "Internal messaging",
                "Notifications",
                "SMS integration",
                "Email integration"
            ]
        }
    ]
    
    for module in modules:
        elements.append(Paragraph(module["name"], heading2_style))
        elements.append(Paragraph(module["description"], normal_style))
        elements.append(Spacer(1, 0.1*inch))
        elements.append(Paragraph("Features:", ParagraphStyle('Bold', parent=normal_style, fontName='Helvetica-Bold')))
        for feature in module["features"]:
            elements.append(Paragraph(f"• {feature}", normal_style))
        elements.append(Spacer(1, 0.2*inch))
    
    elements.append(PageBreak())
    
    # 6. Database Models
    elements.append(Paragraph("6. Database Models", heading1_style))
    elements.append(Paragraph(
        "The system uses a comprehensive database schema with the following main models:",
        normal_style
    ))
    
    models_data = [
        ["Module", "Main Models", "Count"],
        ["Accounts", "User, Campus, AcademicYear, Holiday", "4"],
        ["Students", "Student, StudentDocument, HealthRecord, Promotion", "4"],
        ["Staff", "Staff, Department, Designation, Leave, Attendance", "5"],
        ["Academics", "Class, Section, Subject, Timetable, Attendance, Exam, Grade", "7"],
        ["Finance", "FeeType, FeeStructure, Invoice, Payment, Discount, Expense", "6"],
        ["Library", "Book, BookCategory, BookIssue", "3"],
        ["Transport", "Vehicle, Route, RouteStop, Maintenance", "4"],
        ["Hostel", "Hostel, Room, Facility, Complaint", "4"],
        ["Communication", "Announcement, Message, Notification, SMS, Email", "5"],
    ]
    
    models_table = Table(models_data, colWidths=[1.5*inch, 3.5*inch, 0.7*inch])
    models_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    elements.append(models_table)
    
    elements.append(Spacer(1, 0.3*inch))
    elements.append(Paragraph("Total Models: 42+", ParagraphStyle('Bold', parent=normal_style, fontName='Helvetica-Bold')))
    
    elements.append(PageBreak())
    
    # 7. Forms Created
    elements.append(Paragraph("7. Forms & Templates", heading1_style))
    
    elements.append(Paragraph("7.1 Custom Forms Created", heading2_style))
    forms_list = [
        "StudentForm - Complete student management",
        "StaffForm - Staff/employee management",
        "ClassForm - Class management",
        "SectionForm - Section management",
        "SubjectForm - Subject management",
        "AttendanceForm - Attendance marking",
        "ExaminationForm - Exam creation",
        "HomeworkForm - Assignment management",
        "FeeTypeForm - Fee type management",
        "FeeStructureForm - Fee structure setup",
        "FeeInvoiceForm - Invoice generation",
        "PaymentForm - Payment processing",
        "DiscountForm - Discount management",
        "ExpenseForm - Expense tracking",
        "AnnouncementForm - Announcement creation",
        "MessageForm - Internal messaging",
        "BookForm - Library book management",
        "BookCategoryForm - Book category management",
        "BookIssueForm - Book issue/return",
        "VehicleForm - Vehicle management",
        "RouteForm - Route management",
        "RouteStopForm - Route stop management",
        "HostelForm - Hostel management",
        "RoomForm - Room management",
        "CampusForm - Campus management",
        "AcademicYearForm - Academic year setup",
        "HolidayForm - Holiday management"
    ]
    
    for form in forms_list:
        elements.append(Paragraph(f"• {form}", normal_style))
    
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("Total Forms: 27", ParagraphStyle('Bold', parent=normal_style, fontName='Helvetica-Bold')))
    
    elements.append(PageBreak())
    
    # 8. Sample Data
    elements.append(Paragraph("8. Sample Data", heading1_style))
    elements.append(Paragraph(
        "The system includes a management command to populate sample data for testing:",
        normal_style
    ))
    elements.append(Spacer(1, 0.1*inch))
    elements.append(Paragraph("python manage.py populate_sample_data", code_style))
    
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("Sample Data Created:", heading2_style))
    
    sample_data = [
        ["Data Type", "Count", "Details"],
        ["Campus", "1", "Elite School Main Campus"],
        ["Academic Year", "1", "2024-2025"],
        ["Classes", "10", "Class 1 to Class 10"],
        ["Sections", "20", "A and B for each class"],
        ["Subjects", "5", "Math, English, Science, SST, Urdu"],
        ["Students", "30", "With realistic profiles"],
        ["Announcements", "5", "Sample announcements"],
    ]
    
    sample_table = Table(sample_data, colWidths=[2*inch, 1*inch, 2.5*inch])
    sample_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ]))
    elements.append(sample_table)
    
    elements.append(PageBreak())
    
    # 9. Troubleshooting
    elements.append(Paragraph("9. Troubleshooting", heading1_style))
    
    issues = [
        {
            "issue": "Migration Errors",
            "solution": "Delete db.sqlite3 and run migrations again: python manage.py migrate"
        },
        {
            "issue": "Login Issues",
            "solution": "Create superuser: python manage.py createsuperuser"
        },
        {
            "issue": "Template Not Found",
            "solution": "Check TEMPLATES setting in settings.py and ensure templates directory exists"
        },
        {
            "issue": "Static Files Not Loading",
            "solution": "Run: python manage.py collectstatic"
        },
        {
            "issue": "Port Already in Use",
            "solution": "Use different port: python manage.py runserver 8080"
        }
    ]
    
    for item in issues:
        elements.append(Paragraph(f"Issue: {item['issue']}", ParagraphStyle('Bold', parent=normal_style, fontName='Helvetica-Bold')))
        elements.append(Paragraph(f"Solution: {item['solution']}", normal_style))
        elements.append(Spacer(1, 0.15*inch))
    
    elements.append(PageBreak())
    
    # 10. Contact & Support
    elements.append(Paragraph("10. Contact & Support", heading1_style))
    elements.append(Paragraph(
        "For technical support, feature requests, or bug reports, please contact:",
        normal_style
    ))
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("Email: support@eliteschool.com", normal_style))
    elements.append(Paragraph("Website: www.eliteschool.com", normal_style))
    elements.append(Spacer(1, 0.3*inch))
    elements.append(Paragraph("Documentation Version: 1.0", normal_style))
    elements.append(Paragraph(f"Last Updated: {datetime.now().strftime('%B %d, %Y')}", normal_style))
    
    # Build PDF
    doc.build(elements)
    
    return pdf_filename

if __name__ == "__main__":
    filename = create_documentation_pdf()
    print(f"✅ PDF documentation created successfully: {filename}")
