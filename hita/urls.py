"""hita URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from views import *
import views

admin.autodiscover()

urlpatterns = [
    url(r'^management/', include(admin.site.urls)),
    url(r'^$', views.main, name="home"),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^forgot/', views.forgot, name='forgot'),
    url(r'^register/', views.register, name='register'),
    url(r'^spaces/', views.spaces, name='spaces'),
    url(r'^create/', views.create, name='create'),
    url(r'^create-namespace/', views.create_namespace, name='create-namespace'),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^api/', include('api.urls')),
    url(r'^namespaces/', include('namespaces.urls')),
    url(r'^support/', include('support.urls')),
    url(r'^payment/', include('payment.urls')),
    url(r'^dashboards/', include('dashboards.urls')),
    url(r'^tenant/', include('tenant.urls')),
    url(r'^account/', views.account, name='account'),
    url(r'^billing/', views.billing, name='billing'),
    url(r'^user-settings/', views.user_settings, name='user-settings'),
    url(r'^resources/', views.resources, name='resources'),
]
