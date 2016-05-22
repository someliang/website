from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'images/$', views.images, name='images'),
    url(r'video/$', views.video, name='video'),
    url(r'video/(?P<video_id>[0-9]+)/$', views.video_play, name='play_video'),
    url(r'article/(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'example/$', views.example, name='example')
]