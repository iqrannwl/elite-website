from django.urls import path
from . import views

app_name = 'academics'

urlpatterns = [
    # Classes
    path('classes/', views.class_list, name='class_list'),
    path('classes/add/', views.class_create, name='class_create'),
    path('classes/<int:pk>/edit/', views.class_edit, name='class_edit'),
    path('classes/<int:pk>/delete/', views.class_delete, name='class_delete'),
    
    # Sections
    path('sections/', views.section_list, name='section_list'),
    path('sections/add/', views.section_create, name='section_create'),
    path('sections/<int:pk>/edit/', views.section_edit, name='section_edit'),
    path('sections/<int:pk>/delete/', views.section_delete, name='section_delete'),
    
    # Subjects
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/add/', views.subject_create, name='subject_create'),
    path('subjects/<int:pk>/edit/', views.subject_edit, name='subject_edit'),
    path('subjects/<int:pk>/delete/', views.subject_delete, name='subject_delete'),
    
    # Attendance
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/mark/', views.attendance_mark, name='attendance_mark'),
    path('attendance/<int:pk>/edit/', views.attendance_edit, name='attendance_edit'),
    
    # Exams
    path('exams/', views.exam_list, name='exam_list'),
    path('exams/add/', views.exam_create, name='exam_create'),
    path('exams/<int:pk>/edit/', views.exam_edit, name='exam_edit'),
    path('exams/<int:pk>/delete/', views.exam_delete, name='exam_delete'),
]
