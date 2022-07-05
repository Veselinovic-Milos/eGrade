from dataclasses import field
from django.shortcuts import redirect, render
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from student.views import UserCustomeAcessMixin
from student.models import Student
from .models import MyToDo
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
        return reverse_lazy('mytodos')



class RegisterPage(FormView):
    template_name: str = 'authentication/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user: bool = True
    success_url = reverse_lazy('mytodos')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('mytodos')
        return super(RegisterPage, self).get(*args, **kwargs)

class MyToDoList(UserCustomeAcessMixin, ListView):
    raise_exception: bool = False
    permission_required: any = 'mytodo.view_mytodo'
    permission_denied_message: str = 'Not valid permission group.'
    login_url: any = '/mytodos/'
    redirect_field_name: any = 'next'


    model = MyToDo
    context_object_name = 'mytodo'
    template_name: str = 'mytodo/mytodo_list.html'
    queryset = MyToDo.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MyToDoList, self).get_context_data(**kwargs)
        
        context['mytodo'] = context['mytodo'].filter(student_id=self.request.user.id)
        print(context)
        # next line doesnt need user arg because its already filtred by user in prev line
        context['count'] = context['mytodo'].filter(complete=False).count()
        
        # adding search logic

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['mytodo'] = context['mytodo'].filter(title__startswith=search_input) #filtering with first letter
        
        context['search_input'] = search_input
        print(context)
        return context

class MyToDoDetail(UserCustomeAcessMixin, DetailView):
    raise_exception: bool = False
    permission_required: any = 'mytodo.view_mytodo'
    permission_denied_message: str = 'Not valid permission group.'
    login_url: any = '/mytodo/<int:pk>/'
    redirect_field_name: any = 'next'


    model = MyToDo
    context_object_name = 'mytodo'
    template_name: str = 'mytodo/mytodo_detail.html'

class MyToDoCreate(UserCustomeAcessMixin, CreateView):
    raise_exception: bool = False
    permission_required: any = 'mytodo.add_mytodo'
    permission_denied_message: str = 'Not valid permission group.'
    login_url: any = '/mytodos/'
    redirect_field_name: any = 'next'

    model = MyToDo
    fields = ['title', 'desciptions', 'complete']
    success_url = reverse_lazy('mytodos')
    template_name: str = 'mytodo/mytodo_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MyToDoCreate, self).form_valid(form)

class MyToDoUpdate(UserCustomeAcessMixin, UpdateView):
    raise_exception: bool = False
    permission_required: any = 'mytodo.change_mytodo'
    permission_denied_message: str = 'Not valid permission group.'
    login_url: any = '/mytodos/'
    redirect_field_name: any = 'next'

    model = MyToDo
    fields = ['title', 'desciptions', 'complete']
    success_url = reverse_lazy('mytodos')
    template_name: str = 'mytodo/mytodo_form.html'


class MyToDoDelete(UserCustomeAcessMixin, DeleteView):
    raise_exception: bool = False
    permission_required: any = 'mytodo.delete_mytodo'
    permission_denied_message: str = 'Not valid permission group.'
    login_url: any = '/mytodos/'
    redirect_field_name: any = 'next'

    model = MyToDo
    context_object_name = 'mytodo'
    success_url = reverse_lazy('mytodos')
    template_name: str = 'mytodo/mytodo_confirm_delete.html'
