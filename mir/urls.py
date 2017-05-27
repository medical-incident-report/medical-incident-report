from django.conf.urls import patterns, include, url

from opal.urls import urlpatterns as opatterns
from mir import api

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^mir/incident/(?P<incident_id>[0-9]+)$',
        api.MirApi.as_view({
            'get': 'retrieve'
        }),
        name="mir_api"
    ),
)

urlpatterns += opatterns
