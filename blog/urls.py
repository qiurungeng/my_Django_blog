from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^myblog/$', views.myblog, name='myblog'),
]