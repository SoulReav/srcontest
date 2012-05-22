from django.http import HttpResponse, HttpResponseRedirect
from srcomments.models import SRComments

def srcomments_post(request):
    comment = SRComments()
    comment.user = request.user
    comment.comment = request.POST['comment-text']
    comment.url = request.POST['url_page']
    comment.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
