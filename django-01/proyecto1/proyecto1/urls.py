"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from hello import views as hello_views

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^saludar/?$', hello_views.saludar, name='saludar'),
    url(r'^saludar2/?$', hello_views.saludar2, name='saludar2'),
    url(
        r'saludar3/?$',
        hello_views.saludar3,
        name='saludar3'
    ),
    url(
        r'^saludar/(?P<nombre>\w+)/?$',
        hello_views.saludar_con_nombre,
        name='saludar_con_nombre'
    ),
    url(r'^bootstrap/?$', hello_views.bs, name='bs'),
    url(r'^otrabs/?$', hello_views.otrabs, name='obs'),

]
