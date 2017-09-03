from django.shortcuts import render
from .models import Article


def index(request, t):
    if t == u'0':
        articles = Article.objects.all()
    elif t != u'0':
        articles = Article.objects.filter(type=t)
    return render(request, 'information/index.html', {'articles':articles})


def details(request, tid):
    article = Article.objects.get(id=tid)
    return render(request, 'information/details.html', {'article':article})
