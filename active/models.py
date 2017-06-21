# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField('id', primary_key=True)
    created = models.DateTimeField(u'创建日期')
    updated = models.DateTimeField(u'更新日期')
    title = models.CharField(u'标题', max_length=128)
    author = models.CharField(u'作者', max_length=128, blank=True, null=True)
    content = models.TextField(u'内容')

    class Meta:
        verbose_name_plural=u'公益活动'
