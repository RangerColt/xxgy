# coding=utf-8
from django.shortcuts import render
from .models import *


def index(request, t):
    if t == u'0':
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(type=t)
    return render(request, 'volunteer/index.html', {'articles':articles})


def details(request, vid):
    article = Article.objects.get(id=vid)
    return render(request, 'volunteer/details.html', {'article':article})
