from django.conf.urls import *
from srcomments.views import srcomments_post

urlpatterns = patterns(
    'srcomments.views',
    url(r'^post/$', srcomments_post),
)
