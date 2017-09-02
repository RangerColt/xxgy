# coding: utf-8
from django.db import models

# Create your models here.

class Article(models.Model):
    PROJECT_TYPE_CHOICES = (
            ('1', '公益图书馆'),
            ('2', '阅读推广'),
            ('3', '扶贫助学'),
            ('4', '儿童安全教育'),
            ('5', '女童生理卫生')
            )
    id = models.AutoField(primary_key=True)
    type = models.CharField(u'文章类型', max_length=56, choices=PROJECT_TYPE_CHOICES)
    title = models.CharField(u'标题', max_length=128)
    author = models.CharField(u'作者', max_length=16)
    create = models.DateTimeField(u'创建日期', auto_now=True)
    update = models.DateTimeField(u'更新日期', auto_now=True)
    content = models.TextField(u'内容')


    class Meta:
        verbose_name_plural = u'文章'

