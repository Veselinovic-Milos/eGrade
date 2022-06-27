from dataclasses import field
from django.shortcuts import render, redirect
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Course
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class CustomeLogineView(LoginView):
    template_name: str = 'authentication/login.html'
    fields = '__all__'
    redirect_authenticated_user: bool = True

    def get_success_url(self):
        return reverse_lazy('courses')


class RegisterPage(FormView):
    template_name: str = 'authentication/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user: bool = True
    success_url = reverse_lazy('courses')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('courses')
        return super(RegisterPage, self).get(*args, **kwargs)

class CourseList(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'
    template_name: str = 'course/course_list.html'

class CourseDetail(LoginRequiredMixin, DetailView):
    model = Course
    context_object_name = 'course'
    template_name: str = 'course/course_detail.html'

    def get_form(self):

        form = self.form_class(instance=self.object)
        return form['year']


class CourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('courses')
    template_name: str = 'course/course_form.html'

class CourseUpdate(LoginRequiredMixin, UpdateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('courses')
    template_name: str = 'course/course_form.html'


class CourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    context_object_name = 'course'
    success_url = reverse_lazy('courses')
    template_name: str = 'course/course_confirm_delete.html'