from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogsite.blog.views import PostListView, ContactView


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$',      PostListView.as_view(), name='PostList'),
    url(r'^contact/', ContactView.as_view(), name='Contact'),
    url(r'^admin/', include(admin.site.urls)),
)
