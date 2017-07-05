# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Enroll
from django.contrib import admin

class EnrollAdmin(admin.ModelAdmin):
    model = Enroll
    list_display = ('id', 'title', 'created')
    search_fields = ('title', )
    list_per_page = 15


admin.site.register(Enroll, EnrollAdmin)
