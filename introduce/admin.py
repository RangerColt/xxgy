# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Introduce
from django.contrib import admin

class IntroduceAdmin(admin.ModelAdmin):
    model = Introduce
    list_display = ('id', 'title', 'created')
    search_fields = ('title', )
    list_per_page = 15


admin.site.register(Introduce, IntroduceAdmin)
