from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    isStudent=models.BooleanField(default=False)
    isTeacher = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)

