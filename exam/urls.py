from django.urls import path
from .views import *

urlpatterns = [
    path('exams/', ExamList.as_view(), name='exams-list'),
    path('exam/<int:pk>/', ExamDetail.as_view(), name='exam'),
    path('exam-create/', ExamCreate.as_view(), name='exam-create'),
    path('exam-update/<int:pk>/', ExamUpdate.as_view(), name='exam-update'),
    path('exam-delete/<int:pk>/', ExamDelete.as_view(), name='exam-delete'),
]