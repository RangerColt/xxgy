# coding=utf-8
from django.db import models

class Article(models.Model):
    TYPE_CHOIESE = (
            ('1', u'志愿者风采'),
            ('2', u'志愿者招募'),
            ('3', u'公益大使'),
    )

    id = models.AutoField(primary_key=True)
    type = models.CharField(u'文章类型', max_length=56, choices=TYPE_CHOIESE)
    title = models.CharField(u'标题', max_length=128)
    author = models.CharField('作者', max_length=68)
    create = models.DateTimeField(u'创建日期', auto_now=True)
    update = models.DateTimeField(u'更新日期', auto_now=True)
    content = models.TextField(u'内容')

    class Meta:
        verbose_name_plural = u'志愿者'
