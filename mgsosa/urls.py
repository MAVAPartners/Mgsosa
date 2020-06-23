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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from machina import urls as machina_urls

from frontend import views
from worker import views as worker_view

# Change admin site title
admin.site.site_header = "Administration"
admin.site.site_title = "MGSOSA Admin"

urlpatterns = [
    url(r'^$', views.home_sample, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^donations/$', views.donations, name='donations'),
    url(r'^events/$', views.events, name='pastEvents'),
    url(r'^event-details/$', views.event_details, name='eventDetails'),
    url(r'^events-all/$', views.all_events, name='allEvents'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^qleedo/$', views.qleedo, name='qleedo'),
    url(r'^community/$', views.community, name='community'),
    url(r'^daily-prayer/$', views.dailyPrayer, name='dailyPrayer'),
    url(r'^sample/$', views.home_sample, name='sample'),
    url(r'^sample2/$', views.home_sample_two, name='sample2'),
    url(r'^monitor/$', worker_view.check_server_status, name='monitor'),
    url(r"^admin/", admin.site.urls, name="admin"),
    path(r"forum/", include(machina_urls), name="forum"),
    url(r'^signup/$', views.registration_view, name='signup'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^sginout/$', views.logout_request, name='signout'),
    url(r'^addevent/$', views.event_view, name='addevent'),
    url(r'^listevent/$', views.event_list, name='listevent'),
    url(r'^editevent/(?P<event_id>\d{1,18})/$', views.editevent_view, name='editevent'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
