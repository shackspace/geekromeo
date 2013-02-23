from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from .views import HomeView
import os

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^geekromeo/', include('geekromeo.foo.urls')),

    url(r'^profile/', include('profiles.urls')),

    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('', url(r'^media/(.*)$', 'django.views.static.serve', 
                                    kwargs={'document_root': 
                                            os.path.join(settings.PROJECT_ROOT, 
                                                         'media')}), )
