from django.conf.urls.defaults import *
from view import main, login, logout, descriptionView, laws
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from contest.views import contestPage, contSign, contUnSign, contUpload, contDelete, allContest


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc', name='xmlrpc'),
    url(r'^poll/', include('poll.urls')),
    url(r'^$', main, name ='index'),
    (r'^accounts/login/(?P<error>([a-z]{1,5})?)(/)?$', login),
    (r'^accounts/logout/', logout),
    (r'^laws/$', laws),
    (r'^news/(?P<year>(\d){4})(/)(?P<month>(\d){2})(/)(?P<day>(\d){2})(/)(?P<id>(\d)+)(/)?$', descriptionView),
    (r'^contest/(?P<year>(\d){4})(/)(?P<month>(\d){2})(/)(?P<day>(\d){2})(/)(?P<id>(\d)+)(/)?$', contestPage),
    (r'^contest/sign/(?P<id>(\d)+)(/)?$', contSign),
    (r'^contest/unsign/(?P<id>(\d)+)(/)?$', contUnSign),
    (r'^contest/upload/(?P<id>(\d)+)(/)?$', contUpload),
    (r'^contest/delete/(?P<id>(\d)+)(/)?$', contDelete),
    (r'^contest/$', allContest),
    # Example:
    # (r'^grelka/', include('grelka.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/',include('tinymce.urls')),
    (r'^srcomments/',include('srcomments.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
