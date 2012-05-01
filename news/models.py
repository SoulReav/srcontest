# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_model

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length = 70)
    text_news = tinymce_model.HTMLField()
    date = models.DateField()
    public = models.BooleanField()
    author = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/news/%s" % (self.date.strftime('%Y/%m/%d/') + str(self.id)+'/')
    
    class Meta:
        verbose_name_plural = u"Новости"  