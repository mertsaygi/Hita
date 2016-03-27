from api import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns, url

urlpatterns = patterns('hita.api.views',
    url(r'^$', views.main, name="home"),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^get-tenants/', views.get_tenants, name='get_tenants'),
)
