from django.shortcuts import render
from django.views.generic import ListView, DetailView
from teachers.models import Teacher
from utils import utils


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context={
            'teachers': self.get_queryset(),
            **utils.get_context()
        }
        return context


class TecaherDetailsView(DetailView):
    model = Teacher
    template_name = 'teacher_details.html'
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(utils.get_context())
        return context