# coding : utf-8
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Project, Article


# Register your models here.

class ProjectAdmin(SummernoteModelAdmin):
    list_display = ('pro_type',)
    list_per_page = 10

class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'pro_type', 'author', 'create')
    list_per_page = 10

admin.site.register(Article, ArticleAdmin)
admin.site.register(Project, ProjectAdmin)

