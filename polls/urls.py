from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

from polls.views import StaticView

app_name = 'polls'

urlpatterns= [
    url(r'^$', views.Display, name='Display'),
    url(r'^(?P<id>[0-9]+)/$', views.Detail, name='Detail'),
    url(r'^date/$', views.Datee, name='Datee'),

    url(r'^tempp/$', views.AboutUs.as_view(), name='staticview'),
    url(r'^tem/$', views.Displayy.as_view(), name='login.html'),
    url(r'^login/$', views.login, name='login')
]
