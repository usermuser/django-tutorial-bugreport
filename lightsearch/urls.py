"""
URLs map
"""
#coding: utf-8
from django.conf.urls import url, patterns
from lightsearch.views import search_callback

urlpatterns = patterns('',
    url(r'^$', search_callback, name='lightsearch'),
)
