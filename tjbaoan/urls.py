"""tjbaoan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from website import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admins/$', views.admins),
    #传参如正则，因正则中分了2个组在views中方法需要添加2个参数接收传参
    url(r'^admins/(\w+)/(\w+)$', views.adminsModulesDispathcer),
    url(r'^testpage/', views.testpage),
    url(r'^admins/news/', views.news),
    url(r'^admins/news/add', views.addNews),
    url(r'^index/', views.index),
    url(r'^$', views.index),
    url(r'^joinus$', views.join_us),
    url(r'^regist/$', views.regist),
    url(r'^info/', views.info),
    url(r'^detail/', views.detail),
    url(r'^login/$', views.do_login),
    url(r'^userfuncs/$', views.userfuncs),
    url(r'^adduser/$', views.adduser),
    url(r'^rongyu/$', views.rongyu),
]


