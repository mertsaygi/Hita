# -*- coding: utf-8 -*-
from payment import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns, url

urlpatterns = patterns('hita.payments.views',
    url(r'^$', views.main, name="home"),
    url(r'^success/$', views.success, name="success"),
    url(r'^fail/$', views.fail, name="fail"),
)
