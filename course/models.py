from django.db import models
from exam.models import Exam
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    exams = models.ManyToManyField(Exam, blank=True)
    attedence = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    grades = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title, self.status