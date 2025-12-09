# Sample Data Population Guide

## 📊 Management Command: populate_sample_data

This command populates ALL models in the school management system with realistic dummy data.

### 🚀 How to Run

```bash
# Install Faker first (if not installed)
pip install Faker

# Run the command
python manage.py populate_sample_data
```

### 📦 What Data Gets Created

#### **1. Accounts Module**
- ✅ 2 Campuses (Main Campus, North Campus)
- ✅ 2 Academic Years (2023-2024, 2024-2025)
- ✅ 4 Holidays

#### **2. Staff Module**
- ✅ 5 Departments (Science, Math, English, etc.)
- ✅ 6 Designations (Principal, Teacher, etc.)
- ✅ 15 Staff Members with complete profiles
- ✅ 4 Leave Types
- ✅ 10 Leave Applications

#### **3. Academics Module**
- ✅ 10 Classes (Class 1 to Class 10)
- ✅ 20 Sections (A, B for each class)
- ✅ 8 Subjects (Math, English, Science, etc.)
- ✅ 2 Examinations (First Term, Mid Term)
- ✅ 50 Attendance Records
- ✅ Multiple Homework Assignments

#### **4. Students Module**
- ✅ 50 Students with complete profiles
  - Personal information
  - Parent details
  - Emergency contacts
  - Class and section assignments

#### **5. Finance Module**
- ✅ 5 Fee Types (Tuition, Transport, Library, etc.)
- ✅ Fee Structures for all classes
- ✅ 20 Fee Invoices
- ✅ Payments (Cash, Bank Transfer, etc.)
- ✅ 3 Discounts
- ✅ 5 Expense Categories
- ✅ 20 Expense Records

#### **6. Library Module**
- ✅ 5 Book Categories
- ✅ 30 Books with ISBN, authors, etc.

#### **7. Transport Module**
- ✅ 5 Vehicles (Buses, Vans)
- ✅ 5 Routes with stops
- ✅ 15 Route Stops with timings

#### **8. Hostel Module**
- ✅ 2 Hostels (Boys, Girls)
- ✅ 20 Rooms with occupancy

#### **9. Communication Module**
- ✅ 10 Announcements

### 🎯 Sample Credentials Created

#### **Staff**
- Username: `staff1` to `staff15`
- Password: `staff123`
- Roles: Teachers, Principals, etc.

#### **Students**
- Username: `student1` to `student50`
- Password: `student123`
- Assigned to various classes

### 📊 Total Records Created

- **Users**: 65+ (15 staff + 50 students)
- **Students**: 50
- **Staff**: 15
- **Classes**: 10
- **Sections**: 20
- **Subjects**: 8
- **Invoices**: 20
- **Books**: 30
- **Vehicles**: 5
- **Announcements**: 10
- **And much more!**

### ⚠️ Important Notes

1. **Faker Required**: Install with `pip install Faker`
2. **Idempotent**: Safe to run multiple times (uses get_or_create)
3. **Realistic Data**: Uses Faker for names, addresses, phone numbers
4. **Dependencies**: Creates data in correct order (campuses → classes → students)

### 🔄 Re-running the Command

The command is safe to run multiple times. It uses `get_or_create()` for most models, so:
- Existing data won't be duplicated
- New data will be added where needed
- Some models (like invoices, attendance) will create new records each time

### 🧹 Clean Database First (Optional)

If you want to start fresh:

```bash
# Delete database
rm db.sqlite3

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Populate sample data
python manage.py populate_sample_data
```

### ✅ Verify Data

After running, check:

1. **Dashboard**: http://localhost:8000/school/
   - Should show statistics with real numbers

2. **Students List**: http://localhost:8000/school/students/
   - Should show 50 students

3. **Admin Panel**: http://localhost:8000/admin/
   - All models should have data

### 🎨 What You'll See

- **50 students** with realistic names, emails, phone numbers
- **15 staff members** assigned to departments
- **10 classes** with 2 sections each
- **20 invoices** with payments
- **30 library books** ready to issue
- **5 transport routes** with stops
- **10 announcements** for communication
- **Complete fee structures** for all classes

### 🚀 Next Steps

After populating data:

1. Login and explore the dashboard
2. View student profiles
3. Check fee invoices
4. Browse library books
5. View announcements
6. Test all features with real-looking data!

---

**Command File**: `accounts/management/commands/populate_sample_data.py`

**Usage**: `python manage.py populate_sample_data`
