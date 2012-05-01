from django.conf.urls.defaults import *
from view import main, login, logout, NewsDetailView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc', name='xmlrpc'),
    (r'^$', main),
    (r'^accounts/login/(?P<error>([a-z]{1,5})?)(/)?$', login),
    (r'^accounts/logout/', logout),
    (r'^news/(?P<year>(\d){4})(/)(?P<month>(\d){2})(/)(?P<day>(\d){2})(/)(?P<idd>(\d)+)(/)?$', NewsDetailView),
    (r"^comments/", include("django.contrib.comments.urls")),
    # Example:
    # (r'^grelka/', include('grelka.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/',include('tinymce.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
