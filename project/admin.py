# coding : utf-8
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article


# Register your models here.

class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'create')
    list_per_page = 10

admin.site.register(Article, ArticleAdmin)
