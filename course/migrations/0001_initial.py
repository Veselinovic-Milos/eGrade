# Generated by Django 4.0.5 on 2022-06-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('attedence', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('grades', models.CharField(blank=True, max_length=500, null=True)),
                ('exams', models.ManyToManyField(blank=True, null=True, to='exam.exam')),
            ],
        ),
    ]