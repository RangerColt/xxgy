# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from active.models import *


def index(request):
    articles = Article.objects.all()[:10]
    return render(request, 'home/index.html', {'articles': articles})
