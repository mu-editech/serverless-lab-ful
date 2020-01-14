from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.pic_list, name='pic_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.pic_detail, name='pic_detail'),
    url(r'update/$', views.pics_update, name='pics_update'),
]