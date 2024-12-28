from django.db import models


# Create your models here.
class TestProjectModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="项目名称", help_text="项目名称说明")
    leader = models.CharField(max_length=20, verbose_name="项目负责人", help_text="项目负责人说明")
    create_time = models.DateTimeField(auto_now=True, verbose_name="添加时间", help_text="添加时间说明")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "test_project"
        verbose_name_plural = "项目表"


class TestEnvModel(models.Model):
    project = models.ForeignKey(TestProjectModel, on_delete=models.CASCADE, verbose_name="所属项目id",
                                help_text="所属项目id说明")
    global_variable = models.JSONField(verbose_name="全局变量", default=dict, help_text="环境全局变量", null=True,
                                       blank=True)
    debug_global_variable = models.JSONField(verbose_name="debug模式全局变量", help_text="调试模式全局变量", null=True,
                                             blank=True, default=dict)
    db = models.JSONField(verbose_name="数据库设置", help_text="数据库设置说明", null=True, blank=True, default=dict)
    host = models.CharField(max_length=50, verbose_name="项目主机地址", help_text="项目主机地址说明")
    headers = models.JSONField(verbose_name="请求头", help_text="全局请求头", null=True, blank=True, default=dict)
    global_func = models.CharField(max_length=50, verbose_name="全局工具函数", help_text="全局工具函数脚本", null=True,
                                   blank=True)
    name = models.CharField(max_length=50, verbose_name="测试环境名称", help_text="测试环境名称说明")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "test_env"
        verbose_name_plural = "测试环境表"


class TestFileModel(models.Model):
    file = models.FileField(verbose_name="文件", help_text="文件")
    info = models.JSONField(verbose_name="文件保存的数据信息", help_text="文件保存的数据信息帮助", default=list,
                            blank=True)

    def __str__(self):
        return self.info

    class Meta:
        db_table = "test_file"
        verbose_name_plural = "测试文件表"
