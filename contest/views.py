from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
from contest.models import *

def contestPage(request):
    contest = Contest.objects.all()[0]
    contestants = ", ".join([items.username for items in contest.contestants.all()])
    terms = Terms.objects.filter(contest = contest).all()
    extra = Extra.objects.filter(contest = contest).all()

    cut = contest.description.find('<!--more-->')
    if cut != -1:
        contest.PM = contest.description[cut+11:]
        contest.description = contest.description[0:cut]

    return render_to_response('contest.html',{'contest':contest, 'terms':terms, 'extra':extra, 'contestants':contestants}, RequestContext(request))

