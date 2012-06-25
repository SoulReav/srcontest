from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
from contest.models import *

def contestPage(request, year, month, day, id):
    contest = Contest.objects.all()[int(id)-1]
    contestants = ", ".join([items.username for items in contest.contestants.all()])
    terms = Terms.objects.filter(contest = contest).all()
    extra = Extra.objects.filter(contest = contest).all()

    cut = contest.description.find('<!--more-->')
    if cut != -1:
        contest.PM = contest.description[cut+11:]
        contest.description = contest.description[0:cut]

    return render_to_response('contest.html',{'contest':contest, 'terms':terms, 'extra':extra, 'contestants':contestants}, RequestContext(request))

def contSign (request, id):
    if request.user.is_authenticated():
        contest =  Contest.objects.all()[int(id)-1]
        contest.contestants.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def contUnSign (request, id):
    if request.user.is_authenticated():
        contest =  Contest.objects.all()[int(id)-1]
        contest.contestants.remove(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def contUpload (request, id):
    print request.FILES['file'].read()
