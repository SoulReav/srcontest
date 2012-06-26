from django.core.files.base import ContentFile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
from contest.models import *
from contest.forms import DocumentForm

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
        contest.description = contest.description[0:cut]

    print(contest.works.all())

    uploaded = False

    for i in contest.works.all():
        if i.user == request.user:
            uploaded = True

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
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def contUpload (request, id):
    if request.method == 'POST':
        contest = Contest.objects.get(id=id)
        works = Works()
        works.user = request.user
        works.title = str(id)
        file_content = ContentFile(request.FILES['file'].read())
        works.file.save(request.FILES['file'].name, file_content)
        contest.works.add(works)
        # Redirect to the document list after POST
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
