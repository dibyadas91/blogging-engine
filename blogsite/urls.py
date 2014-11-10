from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', views.PostListView.as_view(), name='PostList'),
    url(r'^contact/', views.ContactView.as_view(), name='Contact'),
    url(r'^about/', views.AboutView.as_view() ,name='About'),
    url(r'^admin/', include(admin.site.urls)),
)
