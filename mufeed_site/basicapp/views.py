from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,TemplateView,
                                    CreateView, UpdateView, DeleteView, ListView, DetailView)

from basicapp.models import Course, Student

class IndexView(TemplateView):
    template_name='basicapp/index.html'

class CourseListView(ListView):
    context_object_name = 'courses'
    model = Course

class CourseDetailView(DetailView):
    context_object_name = 'course_detail'
    model = Course
    template_name = 'basicapp/course_detail.html'

class CourseCreateView(CreateView):
    fields = ('name', 'lecturer', 'level')
    model = Course

class CourseUpdateView(UpdateView):
    fields = ('name','lecturer', 'level',)
    model = Course

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy("basicapp:list")


class StudentCreateView(CreateView):
    fields = ('name', 'age', 'course')
    model = Student

class StudentUpdateView(UpdateView):
    fields =('name', 'age', 'course')
    model = Student
