from space import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns, url

urlpatterns = patterns('hita.space.views',
    url(r'^$', views.main, name="home"),
)
