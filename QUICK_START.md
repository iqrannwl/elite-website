# 🚀 Quick Start Guide - Elite School Management System

## 🎯 Getting Started in 5 Minutes

### Step 1: Access the System

Your server is already running! Access these URLs:

#### 🔐 Login Page
**URL**: http://localhost:8000/accounts/login/

**Credentials**:
- Username: `admin`
- Password: `admin123`

#### 📊 Dashboard
**URL**: http://localhost:8000/school/

#### ⚙️ Admin Panel
**URL**: http://localhost:8000/admin/

---

## 📋 First-Time Setup

### 1. Login to Admin Panel

1. Go to: http://localhost:8000/admin/
2. Login with `admin` / `admin123`
3. You'll see all the school management modules

### 2. Create Your School Campus

1. Click on **"Campuses"** under **ACCOUNTS**
2. Click **"Add Campus"**
3. Fill in:
   - Name: `Elite School Main Campus`
   - Code: `ESC001`
   - Address, City, State, Country
   - Phone and Email
4. Click **"Save"**

### 3. Set Up Academic Year

1. Click on **"Academic Years"** under **ACCOUNTS**
2. Click **"Add Academic Year"**
3. Fill in:
   - Name: `2024-2025`
   - Start Date: `2024-04-01`
   - End Date: `2025-03-31`
   - Campus: Select your campus
   - ✅ Check **"Is Current"**
4. Click **"Save"**

### 4. Create Classes

1. Click on **"Classes"** under **ACADEMICS**
2. Add classes one by one:
   - Name: `Class 1`, Numeric Value: `1`, Campus: Your campus
   - Name: `Class 2`, Numeric Value: `2`, Campus: Your campus
   - Continue for all classes...

### 5. Create Sections

1. Click on **"Sections"** under **ACADEMICS**
2. For each class, add sections:
   - Name: `A`, Class: `Class 1`, Capacity: `40`
   - Name: `B`, Class: `Class 1`, Capacity: `40`
   - Repeat for other classes...

### 6. Add Subjects

1. Click on **"Subjects"** under **ACADEMICS**
2. Add subjects:
   - Code: `MATH`, Name: `Mathematics`
   - Code: `ENG`, Name: `English`
   - Code: `SCI`, Name: `Science`
   - Code: `SST`, Name: `Social Studies`
   - etc.

### 7. Create Fee Types

1. Click on **"Fee Types"** under **FINANCE**
2. Add fee types:
   - Name: `Tuition Fee`, Code: `TF`
   - Name: `Transport Fee`, Code: `TRF`
   - Name: `Library Fee`, Code: `LF`
   - Name: `Exam Fee`, Code: `EF`

### 8. Set Up Fee Structure

1. Click on **"Fee Structures"** under **FINANCE**
2. For each class and fee type:
   - Class: `Class 1`
   - Fee Type: `Tuition Fee`
   - Amount: `5000`
   - Frequency: `Monthly`
   - Academic Year: Your academic year

### 9. Create Users

#### Create a Teacher:
1. Click on **"Users"** under **ACCOUNTS**
2. Click **"Add User"**
3. Fill in:
   - Username: `teacher1`
   - Password: Set password
   - Email: `teacher1@school.com`
   - First Name: `John`
   - Last Name: `Doe`
   - **Role**: `Teacher`
4. Click **"Save"**

#### Create a Student:
1. Click **"Add User"** again
2. Fill in:
   - Username: `student1`
   - Password: Set password
   - Email: `student1@school.com`
   - First Name: `Jane`
   - Last Name: `Smith`
   - **Role**: `Student`
   - Date of Birth, Gender, etc.
4. Click **"Save"**

### 10. Add Student Profile

1. Click on **"Students"** under **STUDENTS**
2. Click **"Add Student"**
3. Fill in:
   - User: Select the student user you created
   - Admission Number: `2024001`
   - Admission Date: Today's date
   - Campus: Your campus
   - Current Class: `Class 1`
   - Section: `A`
   - Father's Name, Phone, etc.
   - Mother's Name, Phone, etc.
   - Emergency Contact details
4. Click **"Save"**

---

## 🎨 Explore the School Management Interface

### Access the Modern UI

1. Go to: http://localhost:8000/school/
2. Login with `admin` / `admin123`
3. You'll see the beautiful dashboard!

### Navigation Menu (Left Sidebar):

- 📊 **Dashboard** - Overview and statistics
- 👥 **Students** - Student management
- 👨‍🏫 **Staff** - Staff management
- 📚 **Academics** - Classes, subjects, timetables
- ✅ **Attendance** - Attendance tracking
- 📝 **Examinations** - Exam management
- 💰 **Finance** - Fee and payment management
- 📖 **Library** - Library management
- 🚌 **Transport** - Transport management
- 🏠 **Hostel** - Hostel management
- 💬 **Communication** - Announcements and messages
- 📊 **Reports** - Various reports
- ⚙️ **Settings** - System settings

### View Students

1. Click **"Students"** in the sidebar
2. You'll see:
   - Search and filter options
   - Statistics cards
   - Beautiful table with all students
   - Actions: View, Edit, Delete

### View Student Details

1. Click the **eye icon** (👁️) on any student
2. You'll see:
   - Student profile with photo
   - Quick statistics
   - Tabs: Personal Info, Academic, Attendance, Documents, Health

---

## 🎯 Common Tasks

### Add a New Student

**Via Admin Panel**:
1. Admin → Students → Add Student
2. Fill in all details
3. Save

**Via Modern Interface**:
1. School → Students → Add New button
2. (This will redirect to admin for now)

### Mark Attendance

1. Admin → Attendance → Add Attendance
2. Select student, date, status
3. Save

### Create Announcement

1. Admin → Announcements → Add Announcement
2. Fill in title, description, type, target audience
3. Set start and end dates
4. Save

### Generate Invoice

1. Admin → Fee Invoices → Add Fee Invoice
2. Select student, academic year
3. Add invoice items (fee types)
4. Save

### Record Payment

1. Admin → Payments → Add Payment
2. Select invoice
3. Enter amount, payment method
4. Save

---

## 📱 Features to Explore

### Dashboard Features:
- ✅ Real-time statistics
- ✅ Attendance overview chart
- ✅ Quick stats cards
- ✅ Recent admissions
- ✅ Recent announcements
- ✅ Upcoming events

### Student Management:
- ✅ Complete student profiles
- ✅ Document upload
- ✅ Health records
- ✅ Parent information
- ✅ Search and filter
- ✅ Bulk operations

### Academic Features:
- ✅ Class and section management
- ✅ Subject assignment
- ✅ Timetable creation
- ✅ Attendance tracking
- ✅ Exam scheduling
- ✅ Grade entry
- ✅ Report cards

### Financial Features:
- ✅ Fee structure setup
- ✅ Invoice generation
- ✅ Payment tracking
- ✅ Discount management
- ✅ Expense tracking
- ✅ Financial reports

---

## 🎨 Customization Tips

### Change Colors:
Edit `templates/school/base.html` and modify CSS variables:
```css
:root {
    --primary-color: #6366f1;  /* Change this */
    --secondary-color: #8b5cf6; /* And this */
}
```

### Add Your Logo:
Replace the icon in the sidebar brand section

### Customize Dashboard:
Edit `templates/school/dashboard.html`

---

## 🔒 Security Best Practices

1. **Change Default Password**:
   ```bash
   python manage.py changepassword admin
   ```

2. **Create Different User Roles**:
   - Create users with different roles
   - Test permissions

3. **Set DEBUG = False** in production

4. **Use Strong Passwords**

---

## 📊 Sample Data

### Quick Sample Data Script:

Create a file `populate_sample.py` in your project root:

```python
# Run: python manage.py shell < populate_sample.py

from accounts.models import User, Campus, AcademicYear
from students.models import Student
from academics.models import Class, Section, Subject

# Create campus
campus = Campus.objects.create(
    name="Elite School",
    code="ES001",
    address="123 Main St",
    city="Karachi",
    state="Sindh",
    country="Pakistan",
    postal_code="75000",
    phone="+92-300-1234567",
    email="info@eliteschool.com"
)

# Create academic year
year = AcademicYear.objects.create(
    name="2024-2025",
    start_date="2024-04-01",
    end_date="2025-03-31",
    is_current=True,
    campus=campus
)

# Create classes
for i in range(1, 11):
    Class.objects.create(
        name=f"Class {i}",
        numeric_value=i,
        campus=campus
    )

print("Sample data created!")
```

---

## 🆘 Troubleshooting

### Can't Login?
- Check username: `admin`
- Check password: `admin123`
- Clear browser cache

### Page Not Found?
- Make sure server is running
- Check URL: http://localhost:8000/school/

### No Data Showing?
- Add sample data via admin panel
- Check filters (reset them)

### Template Not Loading?
- Check if templates directory exists
- Restart server

---

## 📞 Need Help?

### Documentation:
- Main README: `SCHOOL_MANAGEMENT_README.md`
- Implementation Summary: `IMPLEMENTATION_SUMMARY.md`
- This Guide: `QUICK_START.md`

### Admin Panel:
- Full access to all features
- Comprehensive help text
- Inline documentation

---

## 🎉 You're All Set!

Your school management system is ready to use. Start by:

1. ✅ Adding your school data
2. ✅ Creating users
3. ✅ Adding students
4. ✅ Exploring features
5. ✅ Customizing as needed

**Enjoy your new School Management System! 🎓**
