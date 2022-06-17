from django.urls import path
from .views import *

urlpatterns = [
    path('professors', ProfessorList.as_view(), name='professors'),
    path('professor/<int:pk>/', ProfessorDetail.as_view(), name='professor'),
]