# Generated by Django 4.0.5 on 2022-06-17 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='exams',
            field=models.ManyToManyField(blank=True, to='exam.exam'),
        ),
    ]