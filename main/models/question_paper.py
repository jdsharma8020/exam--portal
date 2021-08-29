from django.db import models
from django.forms import ModelForm
from authAccount.models import User
from .question import Question_DB

class Question_Paper(models.Model):
    professor = models.ForeignKey(User, limit_choices_to={'isTeacher': True}, on_delete=models.CASCADE)
    qPaperTitle = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question_DB)

    def __str__(self):
        return f' Question Paper Title :- {self.qPaperTitle}\n'