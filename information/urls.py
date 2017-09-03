# coding=utf-8
from django.conf.urls import url, include
from .views import *

urlpatterns = [
        url(r'information/(?P<t>\d)/$', index, name='information_index'),
        url(r'information/details/(?P<tid>\d)/$', details, name='information_details'),
    ]
