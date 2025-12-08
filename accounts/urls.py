from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Students
    path('students/', views.students_list, name='students'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    
    # Staff
    path('staff/', views.staff_list, name='staff'),
    
    # Academics
    path('academics/', views.academics_view, name='academics'),
    
    # Attendance
    path('attendance/', views.attendance_view, name='attendance'),
    
    # Exams
    path('exams/', views.exams_view, name='exams'),
    
    # Finance
    path('finance/', views.finance_view, name='finance'),
    
    # Library
    path('library/', views.library_view, name='library'),
    
    # Transport
    path('transport/', views.transport_view, name='transport'),
    
    # Hostel
    path('hostel/', views.hostel_view, name='hostel'),
    
    # Communication
    path('communication/', views.communication_view, name='communication'),
    
    # Reports
    path('reports/', views.reports_view, name='reports'),
    
    # Settings
    path('settings/', views.settings_view, name='settings'),
]
