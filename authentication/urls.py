from django.urls import path


from .views import *


urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'), 
    path('login/', CustomeLogineView.as_view(), name='login'),
    ]