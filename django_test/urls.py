from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from log import views as log_views

urlpatterns = patterns('',
    url(r'^$', log_views.LogView.as_view(), name='home'),
    url(r'^logs/delete/(?P<pk>[\w]+)/$', log_views.LogDeleteView.as_view(), name='log-delete'),
    url(r'^logs/$', log_views.LogListView.as_view(), name='log-list'),
    # url(r'^django_test/', include('django_test.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)