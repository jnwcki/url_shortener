"""url_shortener URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from shorten_app.views import IndexView, AllClick, redirect, AllLink, CreateLink, EditLink

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^all/$', AllClick.as_view(), name="all_clicks"),
    url(r'^links/$', AllLink.as_view(), name="all_links"),
    url(r'^accounts/login/$', auth_views.login, name="login"),
    url(r'^accounts/logout/$', auth_views.logout, name="logout"),
    url(r'^create_link/$', CreateLink.as_view(), name="create_link"),
    url(r'^edit/(?P<pk>\w+)', EditLink.as_view(), name="edit_urls"),
    url(r'^(?P<captured_id>\w+)', redirect, name="clicky")
]
