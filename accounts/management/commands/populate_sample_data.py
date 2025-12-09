from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta, date
import random
from faker import Faker

from accounts.models import User, Campus, AcademicYear
from students.models import Student
from academics.models import Class, Section, Subject
from communication.models import Announcement


class Command(BaseCommand):
    help = 'Populate database with sample data'

    def __init__(self):
        super().__init__()
        self.fake = Faker()

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('🚀 Starting to populate sample data...'))
        
        self.create_campus()
        self.create_academic_year()
        self.create_classes_and_sections()
        self.create_subjects()
        self.create_students()
        self.create_announcements()
        
        self.stdout.write(self.style.SUCCESS('\n✅ Successfully populated sample data!'))
        self.stdout.write(self.style.SUCCESS('\n📊 Summary:'))
        self.stdout.write(f'   - Campus: 1')
        self.stdout.write(f'   - Academic Year: 1')
        self.stdout.write(f'   - Classes: 10')
        self.stdout.write(f'   - Sections: 20')
        self.stdout.write(f'   - Subjects: 5')
        self.stdout.write(f'   - Students: 30')
        self.stdout.write(f'   - Announcements: 5')
        self.stdout.write(self.style.SUCCESS('\n🎉 Your system is now populated with sample data!'))

    def create_campus(self):
        self.stdout.write('Creating campus...')
        Campus.objects.get_or_create(
            code='MC001',
            defaults={
                'name': 'Elite School Main Campus',
                'address': '123 Education Street, Block A',
                'city': 'Karachi',
                'state': 'Sindh',
                'country': 'Pakistan',
                'postal_code': '75000',
                'phone': '+92-300-1234567',
                'email': 'main@eliteschool.com',
                'is_active': True
            }
        )
        self.stdout.write(self.style.SUCCESS('   ✅ Campus created'))

    def create_academic_year(self):
        self.stdout.write('Creating academic year...')
        campus = Campus.objects.first()
        
        AcademicYear.objects.get_or_create(
            name='2024-2025',
            campus=campus,
            defaults={
                'start_date': date(2024, 4, 1),
                'end_date': date(2025, 3, 31),
                'is_current': True
            }
        )
        self.stdout.write(self.style.SUCCESS('   ✅ Academic year created'))

    def create_classes_and_sections(self):
        self.stdout.write('Creating classes and sections...')
        campus = Campus.objects.first()
        
        for i in range(1, 11):
            class_obj, created = Class.objects.get_or_create(
                name=f'Class {i}',
                campus=campus,
                defaults={
                    'numeric_value': i,
                    'is_active': True
                }
            )
            
            for section_name in ['A', 'B']:
                Section.objects.get_or_create(
                    name=section_name,
                    class_name=class_obj,
                    defaults={
                        'capacity': 40,
                        'room_number': f'{i}{section_name}'
                    }
                )
        
        self.stdout.write(self.style.SUCCESS('   ✅ 10 classes with 2 sections each created'))

    def create_subjects(self):
        self.stdout.write('Creating subjects...')
        
        subjects = [
            {'code': 'MATH', 'name': 'Mathematics'},
            {'code': 'ENG', 'name': 'English'},
            {'code': 'SCI', 'name': 'Science'},
            {'code': 'SST', 'name': 'Social Studies'},
            {'code': 'URD', 'name': 'Urdu'},
        ]
        
        for subj_data in subjects:
            Subject.objects.get_or_create(
                code=subj_data['code'],
                defaults={
                    'name': subj_data['name'],
                    'is_active': True
                }
            )
        
        self.stdout.write(self.style.SUCCESS('   ✅ 5 subjects created'))

    def create_students(self):
        self.stdout.write('Creating students...')
        campus = Campus.objects.first()
        classes = list(Class.objects.all())
        
        for i in range(30):
            first_name = self.fake.first_name()
            last_name = self.fake.last_name()
            
            user, created = User.objects.get_or_create(
                username=f"student{i+1}",
                defaults={
                    'email': f"{first_name.lower()}.{last_name.lower()}{i}@student.eliteschool.com",
                    'first_name': first_name,
                    'last_name': last_name,
                    'role': User.UserRole.STUDENT,
                    'phone_number': self.fake.phone_number()[:20],
                    'date_of_birth': self.fake.date_of_birth(minimum_age=5, maximum_age=18),
                    'gender': random.choice(['M', 'F']),
                }
            )
            if created:
                user.set_password('student123')
                user.save()
            
            selected_class = random.choice(classes) if classes else None
            sections = list(selected_class.sections.all()) if selected_class else []
            
            Student.objects.get_or_create(
                user=user,
                defaults={
                    'admission_number': f'ADM{str(i+1).zfill(5)}',
                    'admission_date': self.fake.date_between(start_date='-1y', end_date='today'),
                    'campus': campus,
                    'current_class': selected_class,
                    'section': random.choice(sections) if sections else None,
                    'roll_number': str(random.randint(1, 40)),
                    'blood_group': random.choice(['A+', 'B+', 'O+', 'AB+']),
                    'father_name': self.fake.name_male(),
                    'father_phone': self.fake.phone_number()[:20],
                    'mother_name': self.fake.name_female(),
                    'emergency_contact_name': self.fake.name(),
                    'emergency_contact_phone': self.fake.phone_number()[:20],
                    'emergency_contact_relation': 'Father',
                    'status': 'ACTIVE',
                }
            )
        
        self.stdout.write(self.style.SUCCESS('   ✅ 30 students created'))

    def create_announcements(self):
        self.stdout.write('Creating announcements...')
        admin_user = User.objects.filter(role=User.UserRole.SUPER_ADMIN).first()
        campus = Campus.objects.first()
        
        if not admin_user:
            admin_user = User.objects.filter(is_superuser=True).first()
        
        for i in range(5):
            Announcement.objects.create(
                title=self.fake.sentence(nb_words=6),
                description=self.fake.paragraph(),
                announcement_type=random.choice(['GENERAL', 'URGENT', 'EVENT']),
                target_audience=random.choice(['ALL', 'STUDENTS', 'PARENTS']),
                campus=campus,
                start_date=timezone.now().date(),
                end_date=timezone.now().date() + timedelta(days=7),
                created_by=admin_user,
                is_active=True
            )
        
        self.stdout.write(self.style.SUCCESS('   ✅ 5 announcements created'))
