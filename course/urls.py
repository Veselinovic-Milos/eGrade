from django.urls import path
from .views import CourseList, CourseDetail, CourseCreate, CourseUpdate, CourseDelete

urlpatterns = [
    path('courses/', CourseList.as_view(), name='courses-list'),
    path('course/<int:pk>/', CourseDetail.as_view(), name='course'),
    path('course-create/', CourseCreate.as_view(), name='course-create'),
    path('course-update/<int:pk>/', CourseUpdate.as_view(), name='course-update'),
    path('course-delete/<int:pk>/', CourseDelete.as_view(), name='course-delete'),
]