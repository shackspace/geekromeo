from django.conf.urls import patterns, include, url

from .views import ProfileHomeView, ProfileView

urlpatterns = patterns('',
    url(r'^$', ProfileHomeView.as_view(), name='profileshome'),
    url(r'^(?P<slug>[-\w]+)$', ProfileView.as_view(), name='profiledetail'),
)
