from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bugs/', include('bugtracker.urls')),
    url(r'^journal/', include('japp.urls', namespace = 'japp')),
    url(r'^search/', include('lightsearch.urls')),
)
