# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Article
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

class ArticleAdmin(SummernoteModelAdmin):
    model = Article
    list_display = ('title', 'created')
    search_fields = ('title', )
    list_per_page = 15


admin.site.register(Article, ArticleAdmin)
