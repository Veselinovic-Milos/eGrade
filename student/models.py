from django.db import models
from authentication.models import CustomUser
from course.models import Course
from exam.models import Exam

# Create your models here.

class Student(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_query_name='student')
    classYear = models.IntegerField(blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    courses = models.ManyToManyField(Course, related_query_name='student')
    exams = models.ManyToManyField(Exam, related_query_name='student')
    