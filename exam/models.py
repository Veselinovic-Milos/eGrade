from django.db import models

# Create your models here.


class Exam(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    exam_grade = models.CharField(max_length=100, blank=True, null=True)
    exam_date = models.DateTimeField(auto_now=True)
    attempts = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['exam_date']