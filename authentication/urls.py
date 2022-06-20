from django.urls import path

from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [

    path('login/', CustomeLogineView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # Register
    path('register/', RegisterPage.as_view(), name='register'),
    ]