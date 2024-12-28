from django.contrib import admin
from .models import TestFileModel, TestProjectModel, TestEnvModel


# Register your models here.

@admin.register(TestProjectModel)
class TestProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'leader', 'create_time']


@admin.register(TestEnvModel)
class TestEnvAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'global_variable', 'debug_global_variable', 'db', 'host', 'headers', 'global_func',
                    'name']


@admin.register(TestFileModel)
class TestFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'info']
