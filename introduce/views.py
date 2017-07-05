# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    ins = Introduce.objects.first()
    return render(request, 'introduce/index.html', {'ins': ins})
