"""mgsosa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from frontend import views
from worker import views as worker_view

urlpatterns = [
    url(r'^$', views.home_sample, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^donations/$', views.donations, name='donations'),
    url(r'^events/$', views.events, name='events'),
    url(r'^events-all/$', views.all_events, name='allEvents'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^qleedo/$', views.qleedo, name='qleedo'),
    url(r'^community/$', views.community, name='community'),
    url(r'^daily-prayer/$', views.dailyPrayer, name='dailyPrayer'),
    url(r'^sample/$', views.home_sample, name='sample'),
    url(r'^sample2/$', views.home_sample_two, name='sample2'),
    url(r'^monitor/$', worker_view.check_server_status, name='monitor'),
    path('admin/', admin.site.urls),
]
