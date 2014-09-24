from django.conf.urls import patterns, url
from views import PostView, index

urlpatterns = patterns('',
    #url('^(?P<pk>[\w\d]+)/$', PostView.as_view(), name='blog')
    url(r'^$',index, name='index'),
    url(r'^'),
)