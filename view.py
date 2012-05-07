# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import loader, RequestContext
from django.core.urlresolvers import reverse
from news.models import News
from django.core.context_processors import csrf

def NewsDetailView(request, year, month, day, idd):
    DetailNews = News.objects.get(id=idd) 
    return render_to_response('NewsDetail.html', {'detail_news':DetailNews}, RequestContext(request))

def main(request):
    public_news= News.objects.order_by('-dateCreated').filter(publish=True)[0:5]
    return render_to_response('index.html', {'public_news':public_news}, RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def login(request, error):
    
    if request.user.is_authenticated():
        return HttpResponse(u'Спасибо что зашли %s ' % request.user.username)
    
    if request.method == 'POST':
        if request.method == 'POST':
            username = request.POST['login'].lower()
            password = request.POST['password'].lower()
            user = auth.authenticate(username = username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect(reverse(login, kwargs={'error':'error/'}))
           
    return render_to_response('login.html', {'error':error}, RequestContext(request))

    
    