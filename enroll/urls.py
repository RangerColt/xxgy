#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^enroll/$', index, name='enroll_index'),
]
