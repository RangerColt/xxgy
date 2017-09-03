# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from project.models import Article as PA
from volunteer.models import Article as VA
from information.models import Article as IA


def index(request):
    aas = IA.objects.all()[:10]
    bbs = PA.objects.filter(type=2)[:10]
    ccs = PA.objects.filter(type=3)[:10]
    dds = VA.objects.all()[:10]

    return render(request, 'home/index.html', {'aas':aas, 'bbs':bbs, 'ccs':ccs, 'dds':dds})
