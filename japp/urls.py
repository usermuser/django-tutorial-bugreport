# coding: utf-8
from django.conf.urls import patterns, include, url
from .views import PdaChangesListView, PdaChangesDetailView, PdaChangesRegisterView, PdaChangesCreateView
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
    url(r'^$', PdaChangesListView.as_view(), name='japp_index'),
    url(r'^(?P<pk>[0-9]+)/$', PdaChangesDetailView.as_view(), name='japp_detail'),
    url(r'^login/$', 'django.contrib.auth.views.login',
          {"template_name" : "japp_login.html"}, name="japp_login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
          {"next_page" : reverse_lazy('japp_login')}, name="logout"),
    url(r'^register/$', PdaChangesRegisterView.as_view(), name='japp_register'),
    url(r'^add/$', PdaChangesCreateView.as_view(), name='japp_add'),
   # url(r'^last_changes/$', views.last_10_pda_changes, name='last_changes'),
)
