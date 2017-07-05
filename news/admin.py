# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import News
from django.contrib import admin

class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ('id', 'title', 'created')
    search_fields = ('title', )
    list_per_page = 15


admin.site.register(News, NewsAdmin)
