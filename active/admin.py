# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Article
from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('id', 'title', 'created')
    search_fields = ('title', )
    list_per_page = 15


admin.site.register(Article, ArticleAdmin)
