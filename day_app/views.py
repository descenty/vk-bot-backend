from django.forms import model_to_dict
from rest_framework.response import Response
from .models import Student, ScheduleWeek, ScheduleDay, StudyGroup
from rest_framework import permissions, generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from day_app.serializers import ScheduleWeekSerializer, StudentSerializer, ScheduleDaySerializer, StudyGroupSerializer
from day_app.groups_parser import load_study_group


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated, )


class StudyGroupViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = (IsAuthenticated, )


class ScheduleWeekViewSet(viewsets.ModelViewSet):
    queryset = ScheduleWeek.objects.all()
    serializer_class = ScheduleWeekSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        count = self.request.query_params.get('count')
        study_group = self.request.query_params.get('study_group')
        if count is None or study_group is None:
            return []
        else:
            if ScheduleWeek.objects.filter(study_group=study_group).count() == 0:
                if load_study_group(study_group):
                    return ScheduleWeek.objects.filter(count=count, study_group=study_group)
                else:
                    return []
            else:
                return ScheduleWeek.objects.filter(count=count, study_group=study_group)
