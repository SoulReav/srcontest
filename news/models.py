# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_model

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"Категории"

class News(models.Model):
    title = models.CharField(max_length = 140)
    description = tinymce_model.HTMLField()
    dateCreated = models.DateTimeField()
    author = models.ForeignKey(User)
    publish = models.BooleanField()
    categories = models.ForeignKey(Categories)

    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/news/%s" % (self.dateCreated.strftime('%Y/%m/%d/') + str(self.id)+'/')
    
    class Meta:
        verbose_name_plural = u"Новости"

