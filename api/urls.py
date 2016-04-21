from api import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns, url

urlpatterns = patterns('hita.api.views',
    url(r'^$', views.main, name="home"),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^get-spaces/', views.get_spaces, name='get_spaces'),
    url(r'^get-tenants/', views.get_tenants, name='get_tenants'),
    url(r'^delete-tenant/(?P<pk>[0-9]+)$', views.delete_tenant, name='delete_tenant'),
    url(r'^create-tenant/', views.create_tenant, name='create_tenant'),
    url(r'^get-namespaces/(?P<pk>[0-9]+)$', views.get_namespaces, name='get_namespaces'),
    url(r'^create-namespace/', views.create_namespace, name='create_namespace'),
)
