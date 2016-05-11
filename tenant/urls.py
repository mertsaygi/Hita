from tenant import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns, url

urlpatterns = patterns('hita.tenant.views',
    url(r'^(?P<pk>[0-9]+)$', views.main, name="home"),
    url(r'^access/(?P<pk>[0-9]+)$', views.manage_access, name="access"),
    url(r'^settings/(?P<pk>[0-9]+)$', views.tenant_settings, name="settings"),
)
