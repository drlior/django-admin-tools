
from django.conf.urls import url, include

from django.conf import settings
from django.contrib import admin
from django.views import static

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
]
