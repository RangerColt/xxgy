from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request, t):
    if t == u'0':
        articles = Article.objects.all()
    elif t != u'0':
        articles = Article.objects.filter(type=t)
    return render(request, 'project/index.html', {'articles':articles})


def details(request, tid):
    article = Article.objects.get(id=tid)
    return render(request, 'project/detail.html', {'article':article})
