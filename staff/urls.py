from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.staff_list, name='staff_list'),
    path('add/', views.staff_create, name='staff_create'),
    path('<int:pk>/edit/', views.staff_edit, name='staff_edit'),
    path('<int:pk>/delete/', views.staff_delete, name='staff_delete'),
    path('<int:pk>/', views.staff_detail, name='staff_detail'),
    
    # Leave Management
    path('leave/', views.leave_list, name='leave_list'),
    path('leave/add/', views.leave_create, name='leave_create'),
    path('leave/<int:pk>/edit/', views.leave_edit, name='leave_edit'),
    path('leave/<int:pk>/approve/', views.leave_approve, name='leave_approve'),
]
