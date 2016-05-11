from namespaces import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns, url

urlpatterns = patterns('hita.namespaces.views',
    url(r'^(?P<pk>[0-9]+)$', views.main, name="home"),
    url(r'^view/(?P<pk>[0-9]+)/(?P<file>.+)$', views.view_file, name='view_file'),
    url(r'^access/(?P<pk>[0-9]+)$', views.manage_access, name="access"),
    url(r'^settings/(?P<pk>[0-9]+)$', views.namespace_settings, name="settings"),
)
