from django.db import models
from student.models import Student
# Create your models here.
class MyToDo(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=1, blank=True, null=True, related_name='mytodo')
    title = models.CharField(max_length=200)
    desciptions = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta: # sorting method 
        ordering = ['complete']
