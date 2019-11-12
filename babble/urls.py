"""babble URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from accounts.views import login_view, new_view, home_view,file_view,group_view, profile_view, setting_view, myqueries
from . import  settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_view, name = 'login'),
    url(r'^newuser/', new_view, name = 'newuser'),
    url(r'^dashboard', home_view, name = 'dash'),
    url(r'^associations/(?P<pk>\w+)', group_view, name = 'soc'),
    url(r'^resources', file_view, name = 'file'),
    url(r'^profile', profile_view, name = 'me'),
    url(r'^settings', setting_view, name = 'sett'),
    url(r'^myqueries',myqueries,name='mine')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)