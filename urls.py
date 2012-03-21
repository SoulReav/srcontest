from django.conf.urls.defaults import *
from view import main, login, logout, NewsDetailView
import os.path
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    (r'^$', main),
    (r'^accounts/login/(?P<error>([a-z]{1,5})?)(/)?$', login),
    (r'^accounts/logout/', logout),
    (r'^news/(?P<year>(\d){4})(/)(?P<month>(\d){2})(/)(?P<day>(\d){2})(/)(?P<idd>(\d)+)(/)?$', NewsDetailView),
    (r"^comments/", include("django.contrib.comments.urls")),
    (r'^threadedcomments/', include('threadedcomments.urls')),
    # Example:
    # (r'^grelka/', include('grelka.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

site_media = os.path.join(
  os.path.dirname(__file__), 'templates'
)

if settings.DEBUG:
        urlpatterns += patterns('',
            url(r'^media/(.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
        )