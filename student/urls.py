from django.urls import path
from .views import *

urlpatterns = [
    path('students', StudentList.as_view(), name='students'),
    path('student/<int:pk>/', StudentDetail.as_view(), name='student'),
    path('student-create/', StudentCreate.as_view(), name='student-create'),
    path('student-update/<int:pk>/', StudentUpdate.as_view(), name='student-update'),
    path('student-delete/<int:pk>/', StudentDelete.as_view(), name='student-delete'),
]