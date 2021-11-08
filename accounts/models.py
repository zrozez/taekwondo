from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class UserType(models.TextChoices):
        ADMIN = 'admin'
        TEACHER1 = 'teacher1'
        TEACHER2 = 'teacher2'

    user_type = models.CharField(max_length=50, choices=UserType.choices, default=UserType.TEACHER1)

