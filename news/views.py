# -*- coding: utf-8 -*-

# Create your views here.
from django.http import HttpRequest, HttpResponse
from django_xmlrpc.decorators import xmlrpc_func
from news.models import News, Categories
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from datetime import datetime
from xmlrpclib import Fault
from xmlrpclib import DateTime

def authenticate(username, password):
    try:
        user = User.objects.get(username__exact=username)
    except User.DoesNotExist:
        raise Fault('1', 'Username is incorrect.')
    if not user.check_password(password):
        raise Fault('1', 'Password is invalid.')
    if not user.is_staff or not user.is_active:
        raise Fault('2', 'User account unavailable.')
    return user


@xmlrpc_func(returns='string', args=['string', 'string', 'string',])
def get_users_blogs(appKey, username, password):
    user = authenticate(username, password)
    return [{'isAdmin': user.is_superuser,
            'url': 'http://srcontest.us.to/',
            'blogid': '1',
            'blogName': 'srcontest blog'}]


@xmlrpc_func(returns='struct', args=['string', 'string', 'string'])
def get_user_info(apikey, username, password):
    user = authenticate(username, password)
    site = Site.objects.get_current()
    return user_structure(user, site)

@xmlrpc_func(returns='string', args=['string', 'string', 'string', 'struct', 'boolean'])
def new_post(blog_id, username, password, post, publish):
    user = authenticate(username, password)
    item = News()
    item.title = post['title']
    item.description = post['description']
    if post.get('dateCreated'):
        item.dateCreated  = datetime.strptime(str(post['dateCreated']),'%Y%m%dT%H:%M:%S')
    else:
        item.dateCreated = datetime.now().date()
    item.author = user
    item.publish = publish
    item.categories = Categories.objects.get(name=u'Новости сайта')
    item.save()
    return item.pk

@xmlrpc_func(returns='boolean', args=['string', 'string', 'string', 'struct', 'boolean'])
def edit_post(post_id, username, password, post, publish):
    user = authenticate(username, password)
    item = News.objects.get(id=post_id, author=user)
    item.title = post['title']
    item.description = post['description']
    if post.get('dateCreated'):
        item.dateCreated  = datetime.strptime(str(post['dateCreated']),'%Y%m%dT%H:%M:%S')
    else:
        item.dateCreated = datetime.now().date()
    item.author = user
    item.public = publish
    item.categories = Categories.objects.get(name=u'Новости сайта')
    item.save()
    return True

@xmlrpc_func(returns='boolean', args=['string', 'string', 'string', 'string', 'string'])
def delete_post(apikey, post_id, username, password, publish):
    print post_id
    user = authenticate(username, password)
    News.objects.get(id=post_id, author=user).delete()
    return True