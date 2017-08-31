# coding: utf-8
from django.db import models

# Create your models here.

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    PROJECT_TYPE =(
        ('1', '公益图书馆'),
        ('2', '阅读推广'),
        ('3', '扶贫助学'),
        ('4', '儿童安全教育'),
        ('5', '女童生理卫生')
    )
    pro_type = models.CharField(u'项目类型', max_length=16, choices=PROJECT_TYPE) 
    
    class Meta:
        verbose_name_plural = u'项目分类'

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(u'标题', max_length=128)
    author = models.CharField(u'作者', max_length=16)
    create = models.DateTimeField(u'创建日期', auto_now=True)
    update = models.DateTimeField(u'更新日期', auto_now=True)
    content = models.TextField(u'内容')

    pro_type = models.ForeignKey(Project, default='2')

    class Meta:
        verbose_name_plural = u'文章'

