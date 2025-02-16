from django.urls import path
from .views import TeacherListView, TecaherDetailsView

urlpatterns = [
    path('', TeacherListView.as_view(), name='teachers'),
    path('<int:pk>/', TecaherDetailsView.as_view(), name='teacher_details'),
]