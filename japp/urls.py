# coding: utf-8
from django.conf.urls import patterns, include, url
from .views import PdaChangesListView, PdaChangesDetailView

urlpatterns = patterns('',
    url(r'^$', PdaChangesListView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', PdaChangesDetailView.as_view(), name='detail'),
)
