# Generated by Django 3.2.4 on 2021-08-01 14:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_DB',
            fields=[
                ('qno', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=100)),
                ('optionA', models.CharField(max_length=100)),
                ('optionB', models.CharField(max_length=100)),
                ('optionC', models.CharField(max_length=100)),
                ('optionD', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=200)),
                ('professor', models.ForeignKey(limit_choices_to={'groups__name': 'Professor'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Special_Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=10)),
                ('professor', models.ForeignKey(limit_choices_to={'groups__name': 'Professor'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('students', models.ManyToManyField(limit_choices_to={'groups__name': 'Student'}, related_name='student_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question_Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qPaperTitle', models.CharField(max_length=100)),
                ('professor', models.ForeignKey(limit_choices_to={'groups__name': 'Professor'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('questions', models.ManyToManyField(to='main.Question_DB')),
            ],
        ),
        migrations.CreateModel(
            name='Exam_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('total_marks', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('start_time', models.DateTimeField(default=datetime.datetime(2021, 8, 1, 19, 32, 30, 176363))),
                ('end_time', models.DateTimeField(default=datetime.datetime(2021, 8, 1, 19, 32, 30, 176393))),
                ('professor', models.ForeignKey(limit_choices_to={'groups__name': 'Professor'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question_paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='main.question_paper')),
                ('student_group', models.ManyToManyField(related_name='exams', to='main.Special_Students')),
            ],
        ),
    ]
