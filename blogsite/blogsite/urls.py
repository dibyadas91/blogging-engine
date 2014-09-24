from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import PostListView


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$',      PostListView.as_view(), name='PostList'),
    url(r'^admin/', include(admin.site.urls)),

)
