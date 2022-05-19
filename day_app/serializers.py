from rest_framework import serializers
from .models import Student, ScheduleWeek, StudyGroup, ScheduleDay, Subject


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Student
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('count', 'name', 'form', 'audience_name', 'schedule_day', 'teacher')


class ScheduleDaySerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(
        source='subject_set',
        many=True
    )

    class Meta:
        model = ScheduleDay
        fields = ('count', 'subjects')


class ScheduleWeekSerializer(serializers.ModelSerializer):
    schedule_days = ScheduleDaySerializer(
        source='scheduleday_set',
        many=True
    )

    class Meta:
        model = ScheduleWeek
        fields = ('study_group', 'count', 'schedule_days')


class StudyGroupSerializer(serializers.ModelSerializer):
    schedule_weeks = ScheduleWeekSerializer(
        source='scheduleweek_set',
        many=True
    )

    class Meta:
        model = StudyGroup
        fields = ('name', 'schedule_weeks')
