import json
import os.path

from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from interfaceTestPlatform.settings import MEDIA_ROOT
from .serializers import TestProjectModelSerializer, TestEnvModelSerializer, TestFileSerializer
from .models import TestProjectModel, TestEnvModel, TestFileModel
from rest_framework import permissions, status


# Create your views here.


class TestProjectView(viewsets.ModelViewSet):
    queryset = TestProjectModel.objects.all()
    serializer_class = TestProjectModelSerializer
    # 配置鉴权
    permission_classes = [permissions.IsAuthenticated]


class TestEnvView(viewsets.ModelViewSet):
    queryset = TestEnvModel.objects.all()
    serializer_class = TestEnvModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['project']


class TestFiletView(mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = TestFileModel.objects.all()
    serializer_class = TestFileSerializer
    # 配置鉴权
    permission_classes = [permissions.IsAuthenticated]

    # 重写上传方法
    def create(self, request, *args, **kwargs):
        # 判断文件大小和名称是否重复
        size = request.data['file'].size
        name = request.data['file'].name
        content_type = request.data['file'].content_type
        path = os.path.join(MEDIA_ROOT, name)
        if size > 300 * 1024:
            return Response({"message": "文件大小超出300KB"}, status=status.HTTP_400_BAD_REQUEST)
        elif os.path.isfile(path):
            return Response({"message": "重复上传文件"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            request.data['info'] = json.dumps([name, path, content_type])
            return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # 删除文件
        print(self.get_object().info)
        path = self.get_object().info[1]
        result = super().destroy(request, *args, **kwargs)
        os.remove(path)
        return result
