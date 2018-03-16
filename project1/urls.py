"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.contrib import admin
from django.conf.urls import url,include
from blog import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'admin/', admin.site.urls,name='admin'),
    url(r'^$',views.home,name='home'),
    url(r'^message.html/$',views.message,name='message'),
    url(r'^myblog.html/$', views.myblog, name='myblog'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),

    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'',include('comments.urls')),
    url(r'^signup.html/$', views.signup),
    url(r'^logout/', views.logout_view),
    url(r'^save/$', views.save, name='save'),
    # 将 auth 应用中的 urls 模块包含进来
    #url(r'^users/', include('django.contrib.auth.urls')),

    url('^', include('django.contrib.auth.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()