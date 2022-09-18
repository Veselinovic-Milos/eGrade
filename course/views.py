from dataclasses import field
from django.shortcuts import render, redirect
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from professor.models import Professor
from student.models import Student
from .models import Course
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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
    permission_required = 'course.view_course'
    #redirect_field_name: any = 'courses'

class CourseDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Course
    context_object_name = 'course'
    template_name: str = 'course/course_detail.html'
    permission_required = 'course.view_course'
    
    #redirect_field_name: any = 'courses'
    queryset = Course.objects.all()
    
    def get_form(self):
        form = self.form_class(instance=self.object)
        return form['year']


    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        # getting number of students listening exact course and professors name who teaches course
        context['students'] = Student.objects.prefetch_related('course').count()
        context['professor'] = Professor.objects.prefetch_related('professor')
            
        return context


class CourseCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception: bool = False
    permission_required: any = 'course.add_course'
    permission_denied_message: str = 'Not valid permission group.'
    login_url: any = '/courses/'
   
    #redirect_field_name: any = 'courses'

    model = Course
    fields = '__all__'
    success_url = reverse_lazy('courses')
    template_name: str = 'course/course_form.html'

class CourseUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    raise_exception: bool = False
    permission_required: any = 'course.change_course'
    permission_denied_message: str = 'Not valid permission group.'
    login_url: any = '/courses/'
    
    #redirect_field_name: any = 'courses'

    model = Course
    fields = '__all__'
    success_url = reverse_lazy('courses')
    template_name: str = 'course/course_form.html'


class CourseDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    raise_exception: bool = False
    permission_required: any = 'course.delete_course'
    permission_denied_message: str = 'Not valid permission group.'
    login_url: any = '/courses/'

    #redirect_field_name: any = 'courses'

    model = Course
    context_object_name = 'course'
    success_url = reverse_lazy('courses')
    template_name: str = 'course/course_confirm_delete.html'