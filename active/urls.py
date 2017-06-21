#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^active/$', index, name='active_index'),
]
