

from multiprocessing import context
from platform import processor
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from professor.models import Professor
from course.models import Course
from student.models import Student
from .models import Exam
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
        return reverse_lazy('exams')


class RegisterPage(FormView):
    template_name: str = 'authentication/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user: bool = True
    success_url = reverse_lazy('exams')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('exams')
        return super(RegisterPage, self).get(*args, **kwargs)


class ExamList(LoginRequiredMixin, ListView):
    model = Exam
    context_object_name = 'exams'
    template_name: str = 'exam/exam_list.html'


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        # filtering context data- done exams  by student id 
        context['exams'] = context['exams'].filter(id=self.request.user.id)
        
        #search logic
        search_input  = self.request.GET.get('search-area') or ''
        if search_input:    #filtering with first letter
            context['exams'] = context['exams'].filter(title_startswith=search_input)
        context['search_input'] = search_input
        return context




class ExamDetail(LoginRequiredMixin, DetailView):
    model = Exam
    queryset = Exam.objects.all()
    context_object_name = 'exam'
    template_name: str = 'exam/exam_detail.html'
    def get_context_data(self, **kwargs):
        context = super(ExamDetail,self).get_context_data(**kwargs)
        context['course'] = Course.objects.prefetch_related('exams')
        context['student'] = Student.objects.prefetch_related('student')
        context['professor'] = Professor.objects.prefetch_related('professor')
        print(context)
        return context


class ExamCreate(LoginRequiredMixin, CreateView):
    model = Exam
    fields = '__all__'
    success_url = reverse_lazy('exams')
    template_name: str = 'exam/exam_form.html'

class ExamUpdate(LoginRequiredMixin, UpdateView):
    model = Exam
    fields = '__all__'
    success_url = reverse_lazy('exams')
    template_name: str = 'exam/exam_form.html'


class ExamDelete(LoginRequiredMixin, DeleteView):
    model = Exam
    context_object_name = 'exam'
    success_url = reverse_lazy('exams')
    template_name: str = 'exam/exam_confirm_delete.html'
