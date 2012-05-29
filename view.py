# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import loader, RequestContext
from django.core.urlresolvers import reverse
from news.models import News
from contest.models import Contest

def descriptionView(request, year, month, day, id):
    descriptionNews = News.objects.get(id=id)
    return render_to_response('description.html', {'detail_news':descriptionNews}, RequestContext(request))

def main(request):
    public_news= News.objects.order_by('-dateCreated').filter(publish=True)[0:5]
    for p in public_news:
        cut = p.description.find('<!--more-->')
        if cut != -1:
            p.description = p.description[0:cut]
    contest = []
    for i in range(0,3):
        try:
            item = Contest.objects.all()[i]
            item.td = str(item.description.find('</p>')-1)
            contest.append(item)
        except:
            contest.append(u'Отсутствует')

    return render_to_response('index.html', {'public_news':public_news, 'contest':contest}, RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def login(request, error):
    
    if request.user.is_authenticated():
        return HttpResponse(u'Спасибо что зашли %s ' % request.user.username)

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

    
    