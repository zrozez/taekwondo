from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Student(models.Model):
    class StatusType(models.TextChoices):
        REGISTRATION = 'registration'
        ACCEPTED = 'accepted'

    class ColorType(models.TextChoices):
        WHITE = 'white_10'
        WHITE_YELLOW = 'white_yellow_9'
        YELLOW = 'yellow_8'
        YELLOW_GREEN = 'yellow_green_7'
        GREEN = 'green_6'
        GREEN_BLUE = 'green_blue_5'
        BLUE = 'blue_4'
        BLUE_RED = 'blue_red_3'
        RED = 'red_2'
        RED_BLACK = 'red_black_1'
        BLACK_1 = 'black_1dan'

    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='students')
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField()
    fio_parents = models.CharField(max_length = 258)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=258)
    status = models.CharField(max_length=50, choices=StatusType.choices, default=StatusType.REGISTRATION)
    date = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=255, choices=ColorType.choices, default=ColorType.WHITE)

class StudentDocument(models.Model):

    class DocumentType(models.TextChoices):
        BIRTH_CERTIFICATE = 'birth_certificate'
        PARENT_PASSPORT = 'parent_passport'

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=70, choices=DocumentType.choices, default=DocumentType.BIRTH_CERTIFICATE)
    file = models.FileField()