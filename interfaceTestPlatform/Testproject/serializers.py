#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @file name: serializers.py
 @desc:
 @author: xu wang
 @mail: jason_wangxu@163.com
 @date: 2024/12/28 14:06
"""
from rest_framework.serializers import ModelSerializer
from .models import TestEnvModel, TestProjectModel, TestFileModel


class TestEnvModelSerializer(ModelSerializer):
    class Meta:
        model = TestEnvModel
        fields = "__all__"


class TestProjectModelSerializer(ModelSerializer):
    class Meta:
        model = TestProjectModel
        fields = "__all__"


class TestFileSerializer(ModelSerializer):
    class Meta:
        model = TestFileModel
        fields = "__all__"
