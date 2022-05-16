from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    study_group = models.CharField(max_length=10, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)