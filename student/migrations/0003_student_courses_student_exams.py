# Generated by Django 4.0.5 on 2022-06-27 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_remove_course_students_alter_course_exams'),
        ('exam', '0001_initial'),
        ('student', '0002_remove_student_courses_remove_student_exams_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='student', to='course.course'),
        ),
        migrations.AddField(
            model_name='student',
            name='exams',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='student', to='exam.exam'),
        ),
    ]