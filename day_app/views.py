from django.forms import model_to_dict
from rest_framework.response import Response
from .models import Student
from rest_framework import permissions, generics, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from day_app.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated, )
