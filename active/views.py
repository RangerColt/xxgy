# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

# Create your views here.

# 公益活动列表页
def index(request):
    articles = Article.objects.all()
    return render(request, 'active/index.html', {'articles':articles})


# 公益活动详情页
def details(request):
    id = request.GET.get('id')
    article = Article.objects.get(id=id)
    return render(request, 'active/details.html', {'article': article})
