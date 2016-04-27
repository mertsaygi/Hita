from api import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns, url

urlpatterns = patterns('hita.api.views',
    url(r'^$', views.main, name="home"),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^upload/(?P<pk>[0-9]+)$', views.upload_file, name='upload_file'),
    url(r'^get-files/(?P<pk>[0-9]+)$', views.get_files, name='get_files'),
    url(r'^delete-tenant/(?P<pk>[0-9]+)$', views.delete_tenant, name='delete_tenant'),
    url(r'^create-tenant/', views.create_tenant, name='create_tenant'),
    url(r'^create-single-namespace/(?P<pk>[0-9]+)$', views.create_single_namespace, name='create_namespace'),
    url(r'^create-namespace/(?P<pk>[0-9]+)$', views.create_namespace, name='create_namespace'),
)
