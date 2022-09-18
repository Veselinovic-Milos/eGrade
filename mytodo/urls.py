from django.urls import path
from .views import *

urlpatterns = [
    path('mytodos/', MyToDoList.as_view(), name='mytodos-list'),
    path('mytodo/<int:pk>/', MyToDoDetail.as_view(), name='mytodo'),
    path('mytodo-create/', MyToDoCreate.as_view(), name='mytodo-create'),
    path('mytodo-update/<int:pk>/', MyToDoUpdate.as_view(), name='mytodo-update'),
    path('mytodo-delete/<int:pk>/', MyToDoDelete.as_view(), name='mytodo-delete'),
]