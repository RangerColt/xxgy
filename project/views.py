from django.shortcuts import render
from .models import Article

# Create your views here.

def security(request):
    articles = Article.objects.filter(pro_type__exact='2')
    context = {'articles': articles}
   
    return render(request, 'project/security.html', context)

