
from django.middleware.csrf import get_token
from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View, generic
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.views import redirect_to_login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect


# Create your views here.
@method_decorator(csrf_protect, name='dispatch')
class RegisterPage(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/register.html'
    redirect_authenticated_user: bool = True
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('student/')
        return super(RegisterPage, self).get(*args, **kwargs)

@method_decorator(ensure_csrf_cookie, name='dispatch')
class CustomeLogineView(LoginView):
    template_name = 'authentication/login.html'
    fields = '__all__'
    redirect_authenticated_user: bool = True
    success_url= reverse_lazy('student/')



class GetCSRFToken(View):

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        """Return a empty response with the token CSRF.

        Returns
        -------
        Response
            The response with the token CSRF as a cookie.
        """
        response = JsonResponse({'csrf_token': 'token is set'})
        response['X-CSRFToken'] = get_token(request)
        return response['X-CSRFToken']


""" 
Custome User Mixin for restricting Permissions by Group of user.
class UserCustomeAcessMixin(PermissionRequiredMixin):
    def dispatch(self, request: HttpRequest, *args: any, **kwargs: any) -> HttpResponseBadRequest:
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('/')
        return super(UserCustomeAcessMixin, self).dispatch(request, *args, **kwargs)"""