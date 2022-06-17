from django.db import models
from authentication.models import CustomUser
from course.models import Course

# Create your models here.

class Professor(models.Model):
    professor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_query_name='professor')
    
    def __str__(self):
        return self.professor.get_full_name()