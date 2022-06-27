from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from .models import Professor
from django.urls import reverse_lazy
from django.shortcuts import redirect

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
        return reverse_lazy('professors')
class RegisterPage(FormView):
    template_name: str = 'authentication/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user: bool = True
    success_url = reverse_lazy('professors')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('professors')
        return super(RegisterPage, self).get(*args, **kwargs)

class ProfessorList(LoginRequiredMixin, ListView):
    model = Professor
    context_object_name = 'professors'
    template_name: str = 'professor/professor_list.html'
class ProfessorDetail(LoginRequiredMixin, DetailView):
    model = Professor
    context_object_name = 'professor'
    template_name: str = 'professor/professor_detail.html'


#there is no logic for CUD and list view for Professor
# That should be manageable through admin
