from dataclasses import field

from django.http import HttpResponseBadRequest, HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from course.models import Course
from exam.models import Exam
from .models import Student
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class CustomeLogineView(LoginView):
    template_name: str = 'authentication/login.html'
    fields = '__all__'
    redirect_authenticated_user: bool = True

    def get_success_url(self):
        return reverse_lazy('students')



class RegisterPage(FormView):
    template_name: str = 'authentication/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user: bool = True
    success_url = reverse_lazy('students')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('students')
            
        return super(RegisterPage, self).get(*args, **kwargs)

# Custome User Mixin for restricting Permissions by Group of user.
class UserCustomeAcessMixin(PermissionRequiredMixin):
    def dispatch(self, request: HttpRequest, *args: any, **kwargs: any) -> HttpResponseBadRequest:
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('/students')
        return super(UserCustomeAcessMixin, self).dispatch(request, *args, **kwargs)   

class StudentList(LoginRequiredMixin, ListView):

    model = Student
    context_object_name = 'students'
    template_name: str = 'student/student_list.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = context['students'].filter(student_id=self.request.user.id)
        # next line doesnt need user arg because its already filtred by user in prev line
        context['count'] = context['students'].filter(id=True).count()
        
        # adding search logic

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['students'] = context['students'].filter(title__startswith=search_input) #filtering with first letter
        
        context['search_input'] = search_input
        return context

class StudentDetail(UserCustomeAcessMixin, DetailView):
    raise_exception: bool = False
    permission_required: any = 'student.view_student'
    permission_denied_message: str = 'Not valid permission group.'
    login_url: any = '/student/<int:pk>/'
    redirect_field_name: any = 'next'

    model = Student
    context_object_name = 'student'
    template_name: str = 'student/student_detail.html'
    queryset = Student.objects.all() 

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super(StudentDetail, self).get_context_data(**kwargs)
        context['course'] = Course.objects.prefetch_related('course')
        context['exam'] = Exam.objects.prefetch_related('student')
        
        return context



class StudentCreate(UserCustomeAcessMixin, CreateView):
    raise_exception: bool = False
    permission_required: any = 'students.add_students'
    permission_denied_message: str = 'Not valid permission group.'
    login_url: any = '/students/'
    redirect_field_name: any = 'next'

    model = Student
    fields = ['classYear', 'semester', 'courses', 'exams']
    success_url = reverse_lazy('students')
    template_name: str = 'student/student_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(StudentCreate, self).form_valid(form)

class StudentUpdate(UserCustomeAcessMixin, UpdateView):
    raise_exception: bool = False
    permission_required: any = 'student.change_student'
    permission_denied_message: str = 'Not valid permission group.'
    login_url: any = '/student/<int:pk>/'
    redirect_field_name: any = 'next'


    model = Student
    fields = ['classYear', 'semester', 'courses', 'exams']
    success_url = reverse_lazy('students')
    template_name: str = 'student/student_form.html'


class StudentDelete(UserCustomeAcessMixin, DeleteView):
    raise_exception: bool = False
    permission_required: any = 'students.delete_students'
    permission_denied_message: str = 'Not valid permission group.'
    login_url: any = '/student/<int:pk>/'
    redirect_field_name: any = 'next'


    model = Student
    context_object_name = 'student'
    success_url = reverse_lazy('students')
    template_name: str = 'student/student_confirm_delete.html'
