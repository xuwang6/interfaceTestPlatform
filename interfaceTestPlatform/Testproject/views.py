from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TestProjectModelSerializer, TestEnvModel, TestFileSerializer
from .models import TestProjectModel, TestEnvModel, TestFileModel


# Create your views here.


class TestProjectView(viewsets.ModelViewSet):
    queryset = TestProjectModel.objects.all()
    serializer_class = TestProjectModelSerializer
