# # -*- encoding: utf8 -*-

from django.db import models

# 用于存储平台上各项目的基础数据 ProBaseTable
class ProjectBaseInfo(models.Model):
    pro_name = models.CharField('项目名称', max_length=50, unique=True)
    description = models.CharField('项目描述', max_length=200, default=None, null=True)
    item_name = models.CharField('项目映射值', max_length=500, default=None, null=True)
    max_key = models.CharField('当前最大key值', max_length=50, default='0')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

# 各项目的详细信息
class ProjectItemValues(models.Model): 
    pro_name = models.ForeignKey(ProjectBaseInfo, related_name='pro_info', help_text='项目基础信息表外键')
    item_key = models.CharField('记录的key值', max_length=50)
    values = models.CharField('记录值', db_index=True, max_length=1000, default=' ')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    

