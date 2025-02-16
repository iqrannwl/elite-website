from django.shortcuts import render
from courses.models import CoursePage
from django.views.generic import ListView, DetailView
from utils import utils

def courses_page(request):
    courses = CoursePage.objects.all()
    return render(request, 'courses.html', {
        'courses': courses
    })

class CourseListView(ListView):
    model = CoursePage
    template_name = 'courses.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context={
            'courses': self.get_queryset(),
            **utils.get_context()
        }
        return context


class CourseDetailView(DetailView):
    model = CoursePage
    template_name = 'course.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(utils.get_context())
        return context
