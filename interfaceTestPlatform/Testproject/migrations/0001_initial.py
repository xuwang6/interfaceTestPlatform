# Generated by Django 4.2 on 2024-12-28 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text='文件', upload_to='', verbose_name='文件')),
                ('info', models.JSONField(blank=True, default=list, help_text='文件保存的数据信息帮助', verbose_name='文件保存的数据信息')),
            ],
            options={
                'verbose_name_plural': '测试文件表',
                'db_table': 'test_file',
            },
        ),
        migrations.CreateModel(
            name='TestProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='项目名称说明', max_length=50, verbose_name='项目名称')),
                ('leader', models.CharField(help_text='项目负责人说明', max_length=20, verbose_name='项目负责人')),
                ('create_time', models.DateTimeField(auto_now=True, help_text='添加时间说明', verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '项目表',
                'db_table': 'test_project',
            },
        ),
        migrations.CreateModel(
            name='TestEnvModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('global_variable', models.JSONField(blank=True, default=dict, help_text='环境全局变量', null=True, verbose_name='全局变量')),
                ('debug_global_variable', models.JSONField(blank=True, default=dict, help_text='调试模式全局变量', null=True, verbose_name='debug模式全局变量')),
                ('db', models.JSONField(blank=True, default=dict, help_text='数据库设置说明', null=True, verbose_name='数据库设置')),
                ('host', models.CharField(help_text='项目主机地址说明', max_length=50, verbose_name='项目主机地址')),
                ('headers', models.JSONField(blank=True, default=dict, help_text='全局请求头', null=True, verbose_name='请求头')),
                ('global_func', models.CharField(blank=True, help_text='全局工具函数脚本', max_length=50, null=True, verbose_name='全局工具函数')),
                ('name', models.CharField(help_text='测试环境名称说明', max_length=50, verbose_name='测试环境名称')),
                ('project', models.ForeignKey(help_text='所属项目id说明', on_delete=django.db.models.deletion.CASCADE, to='Testproject.testprojectmodel', verbose_name='所属项目id')),
            ],
            options={
                'verbose_name_plural': '测试环境表',
                'db_table': 'test_env',
            },
        ),
    ]
