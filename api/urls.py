from api import views
from django.conf import settings
from django.conf.urls import include
from django.http import *
from django.conf.urls import patterns, url

urlpatterns = patterns('hita.api.views',
    url(r'^$', views.main, name="home"),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    # Folder Processes
    url(r'^folder/create/', views.create_folder, name='create_folder'),
    url(r'^folder/delete/', views.delete_folder, name='delete_folder'),
    # File Processes
    url(r'^files/(?P<pk>[0-9]+)/(?P<file>.+)$', views.get_file, name='get_file'),
    url(r'^files/upload/(?P<pk>[0-9]+)$', views.upload_file, name='upload_file'),
    url(r'^files/list/(?P<pk>[0-9]+)$', views.get_files, name='get_files'),
    url(r'^files/delete/', views.delete_files, name='delete_files'),
    # Tenant Processes
    url(r'^tenant/delete/(?P<pk>[0-9]+)$', views.delete_tenant, name='delete_tenant'),
    url(r'^tenant/(?P<pk>[0-9]+)$', views.get_tenant_info, name='get_tenant_info'),
    url(r'^tenant/create/', views.create_tenant, name='create_tenant'),
    # Namespace Processes
    url(r'^namespace/create-without-tenant/(?P<pk>[0-9]+)$', views.create_single_namespace, name='create_namespace'),
    url(r'^namespace/create/(?P<pk>[0-9]+)$', views.create_namespace, name='create_namespace'),
    url(r'^namespace/delete/(?P<pk>[0-9]+)$', views.delete_namespace, name='delete_namespace'),
)
