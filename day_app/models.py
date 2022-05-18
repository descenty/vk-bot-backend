from django.contrib.auth.models import User
from django.db import models
from django.core.validators import int_list_validator


class StudyGroup(models.Model):
    name = models.CharField(max_length=10, primary_key=True)


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    study_group = models.ForeignKey(StudyGroup, db_index=True, on_delete=models.CASCADE)


class ScheduleWeek(models.Model):
    study_group = models.ForeignKey(StudyGroup, db_index=True, on_delete=models.CASCADE)
    count = models.IntegerField(primary_key=True)


class WeekDay(models.Model):
    name = models.CharField(max_length=25, primary_key=True)


class ScheduleDay(models.Model):
    name = models.ForeignKey(WeekDay, db_index=True, on_delete=models.CASCADE)
    schedule_week = models.ForeignKey(ScheduleWeek, db_index=True, on_delete=models.CASCADE)


class DayPeriod(models.Model):
    period = models.CharField(max_length=15, primary_key=True)


class ScheduleDayPeriod(models.Model):
    schedule_day = models.ForeignKey(ScheduleDay, db_index=True, on_delete=models.CASCADE)
    period = models.ForeignKey(DayPeriod, db_index=True, on_delete=models.CASCADE)


class Lesson(models.Model):
    index = models.IntegerField(primary_key=True)
    period = models.ForeignKey(ScheduleDayPeriod, db_index=True, on_delete=models.CASCADE)


class Teacher(models.Model):
    name = models.CharField(max_length=50, primary_key=True)


class Subject(models.Model):
    name = models.CharField(max_length=90, blank=True)
    form = models.CharField(max_length=10, blank=True)
    teacher = models.ForeignKey(Teacher, db_index=True, on_delete=models.CASCADE)
    audience_name = models.CharField(max_length=10, blank=True)
    on_weeks = models.CharField(max_length=50, validators=[int_list_validator])
    test_weeks = models.CharField(max_length=50, validators=[int_list_validator])
    lesson = models.ForeignKey(Lesson, db_index=True, on_delete=models.CASCADE)
