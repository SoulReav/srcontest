# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_model

def make_upload_path(instance, filename):
    """Generates upload path for FileField"""
    return u"uploads/%s/%s" % (instance.title,instance.user.username+'.rtf')

class Works(models.Model):
    title = models.CharField(max_length=140)
    user = models.ForeignKey(User)
    file = models.FileField(upload_to=make_upload_path)
    uploaded_date = models.DateTimeField(auto_now_add=True)

class Contest(models.Model):
    title = models.CharField(max_length=140, verbose_name=u'Заголовок конкурса')
    description = tinymce_model.HTMLField(verbose_name=u'Описание')
    genre = models.CharField(max_length=140,verbose_name=u'Жанр')
    startdate = models.DateField(verbose_name=u'Дата старта')
    enddate = models.DateField(verbose_name=u'Дата завершения')
    contestants = models.ManyToManyField(User)
    works = models.ManyToManyField(Works, null=True, blank=True)
    moderate = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/contest/%s" % (self.startdate.strftime('%Y/%m/%d/') + str(self.id)+'/')

class Terms(models.Model):
    contest = models.ForeignKey(Contest)
    text = models.CharField(max_length=300, verbose_name=u'Обязательные требования')

class Extra(models.Model):
    contest = models.ForeignKey(Contest)
    text = models.CharField(max_length=300,verbose_name=u'Приветствуется')