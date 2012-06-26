# -*- coding: utf-8 -*-

from django.core.files.base import ContentFile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
from contest.models import *
import datetime

def handle_uploaded_file(f):
    destination = open('files/media/uploads/1.txt', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def contestPage(request, year, month, day, id):
    contest = Contest.objects.all()[int(id)-1]
    contestants = ", ".join([items.username for items in contest.contestants.all()])
    terms = Terms.objects.filter(contest = contest).all()
    extra = Extra.objects.filter(contest = contest).all()

    cut = contest.description.find('<!--more-->')
    if cut != -1:
        contest.PM = contest.description[cut+11:]
        contest.Tdescription = contest.description[3:cut-6]
    print(contest.works.all())

    uploaded = False

    for i in contest.works.all():
        if i.user == request.user:
            uploaded = True

    now = datetime.datetime.now().date()

    if contest.stage <> 'VT' and contest.stage <> 'CM':
        if contest.enddate <= now:
            contest.stage = 'MD'
            contest.save()
        else:
            contest.stage = 'CT'
            contest.save()

    return render_to_response('contest.html',{'contest':contest, 'terms':terms, 'extra':extra, 'contestants':contestants, 'uploaded': uploaded}, RequestContext(request))

def contSign (request, id):
    if request.user.is_authenticated():
        contest =  Contest.objects.all()[int(id)-1]
        contest.contestants.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def contUnSign (request, id):
    if request.user.is_authenticated():
        contest =  Contest.objects.all()[int(id)-1]
        contest.contestants.remove(request.user)
        if contest.works.count() <> 0:
            i = contest.works.get(user = request.user)
            i.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def contUpload (request, id):
    if request.method == 'POST':
        contest = Contest.objects.get(id=id)
        works = Works()
        works.user = request.user
        works.patch = str(id)
        works.title = request.POST['work-title']
        if request.FILES['file'].name[-3:] <> 'rtf':
           return HttpResponse('Не верный формат загружаемого файла. Поддерживается только .RTF')
        file_content = ContentFile(request.FILES['file'].read())
        works.file.save(request.FILES['file'].name, file_content)
        contest.works.add(works)
        # Redirect to the document list after POST
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

def contDelete (request,id):
    contest = Contest.objects.get(id=id)
    i = contest.works.get(user = request.user)
    i.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])