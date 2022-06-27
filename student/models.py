from django.db import models
from authentication.models import CustomUser
#
from course.models import Course
from exam.models import Exam
#from mytodo.models import MyToDo
# Create your models here.

class Student(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='student')
    classYear = models.IntegerField(blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True ,related_name='course')
    exams = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=True, null=True ,related_name='student')
    #mytodos = models.ForeignKey(MyToDo, on_delete=models.CASCADE, blank=True, null=True, related_query_name='mytodo')
    