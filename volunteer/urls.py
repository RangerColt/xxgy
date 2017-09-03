from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^volunteer/(?P<t>\d)/$', index, name='volunteer_index'),
    url(r'^volunteer/details/(?P<vid>\d)/$', details, name='volunteer_details'),
]
