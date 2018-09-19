"""django_test URL Configuration

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
from app1.views import home, test1, test2, test3, Test1, Test2, Test3, Test4

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^test1/$', test1),
    url(r'^test2/$', test2),
    url(r'^test3/(?P<num>[0-9]+)/$', test3),
    url(r'^Test1$', Test1.as_view()),
    url(r'^Test2/$', Test2.as_view()),
    url(r'^Test3/(?P<pk>[0-9]+)$', Test3.as_view()),
    url(r'^Test4/$', Test4.as_view()),

]

