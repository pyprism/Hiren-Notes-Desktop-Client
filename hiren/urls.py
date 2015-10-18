"""hiren URL Configuration

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
from pirate import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r"^logout$", views.logout),
    url(r"^dashboard$", views.dashboard),
    url(r"^dashboard/add$", views.add),
    url(r"^category/(?P<category>[^\.]+)/post/(?P<slug>[^\.]+)/delete", views.content_delete),
    url(r"^category/(?P<category>[^\.]+)/post/(?P<slug>[^\.]+)/", views.single_content),
    url(r"^category/(?P<category>[^\.]+)/", views.category_content),
    url(r"^contact", views.contact),
]
