from django.contrib.auth.models import User
from django.db import models
from django.core.validators import int_list_validator


class StudyGroup(models.Model):
    name = models.CharField(max_length=10, primary_key=True)


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    study_group = models.ForeignKey(StudyGroup, db_index=True, on_delete=models.CASCADE)


class ScheduleWeek(models.Model):
    count = models.IntegerField()
    study_group = models.ForeignKey(StudyGroup, db_index=True, on_delete=models.CASCADE)


class ScheduleDay(models.Model):
    count = models.IntegerField()
    schedule_week = models.ForeignKey(ScheduleWeek, db_index=True, on_delete=models.CASCADE)


class Teacher(models.Model):
    name = models.CharField(max_length=50, primary_key=True)


class Subject(models.Model):
    count = models.IntegerField(null=False)
    schedule_day = models.ForeignKey(ScheduleDay, db_index=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=90, blank=True)
    form = models.CharField(max_length=10, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, db_index=True, on_delete=models.CASCADE, null=True)
    audience_name = models.CharField(max_length=10, blank=True, null=True)


class DataLastUpdate(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    last_update = models.DateTimeField()