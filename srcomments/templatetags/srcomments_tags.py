from django import template
from srcontest.srcomments.models import SRComments
from srcontest.news.models import News
from django.http import HttpRequest

register = template.Library()

@register.inclusion_tag('srcomments.html', takes_context=True)
def show_srcomments(context):
    comments = SRComments.objects.order_by('dateCreated').filter(url= context['request'].get_full_path()).all()
    return {'MEDIA_URL': context['MEDIA_URL'], 'comments':comments, 'user':context['user'], 'url':context['request'].get_full_path()}