from dataclasses import field
from django.shortcuts import redirect, render
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
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

class MyToDoList(LoginRequiredMixin, ListView):
    model = MyToDo
    context_object_name = 'mytodo'
    template_name: str = 'mytodo/mytodo_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['mytodo'] = context['mytodo'].filter(student_id=self.request.user.id)
        # next line doesnt need user arg because its already filtred by user in prev line
        context['count'] = context['mytodo'].filter(complete=False).count()
        
        # adding search logic

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['mytodos'] = context['mytodos'].filter(title__startswith=search_input) #filtering with first letter
        
        context['search_input'] = search_input
        return context

class MyToDoDetail(LoginRequiredMixin, DetailView):
    model = MyToDo
    context_object_name = 'mytodo'
    template_name: str = 'mytodo/mytodo_detail.html'

class MyToDoCreate(LoginRequiredMixin, CreateView):
    model = MyToDo
    fields = ['title', 'desciptions', 'complete']
    success_url = reverse_lazy('mytodos')
    template_name: str = 'mytodo/mytodo_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MyToDoCreate, self).form_valid(form)

class MyToDoUpdate(LoginRequiredMixin, UpdateView):
    model = MyToDo
    fields = ['title', 'desciptions', 'complete']
    success_url = reverse_lazy('mytodos')
    template_name: str = 'mytodo/mytodo_form.html'


class MyToDoDelete(LoginRequiredMixin, DeleteView):
    model = MyToDo
    context_object_name = 'mytodo'
    success_url = reverse_lazy('mytodos')
    template_name: str = 'mytodo/mytodo_confirm_delete.html'
