from django.conf.urls import patterns, include, url

from .views import ProfileHomeView

urlpatterns = patterns('',
    url(r'^$', ProfileHomeView.as_view(), name='profileshome'),
)
