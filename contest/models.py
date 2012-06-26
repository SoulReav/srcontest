# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_model
from django.db.models.signals import post_delete

def make_upload_path(instance, filename):
    """Generates upload path for FileField"""
    return u"uploads/%s/%s" % (instance.patch,instance.user.username+'.rtf')


class Works(models.Model):
    title = models.CharField(max_length=140)
    user = models.ForeignKey(User)
    file = models.FileField(upload_to=make_upload_path)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    patch = models.CharField(max_length=140)

def delete_file(sender, **kwargs):
    mf = kwargs.get("instance")
    mf.file.delete(save=False)

post_delete.connect(delete_file, Works)

class Contest(models.Model):
    title = models.CharField(max_length=140, verbose_name=u'Заголовок конкурса')
    imglogo = models.CharField(max_length=140, verbose_name=u'Картинка к заголовку')
    description = tinymce_model.HTMLField(verbose_name=u'Описание')
    genre = models.CharField(max_length=140,verbose_name=u'Жанр')
    startdate = models.DateField(verbose_name=u'Дата старта')
    enddate = models.DateField(verbose_name=u'Дата завершения')
    contestants = models.ManyToManyField(User)
    works = models.ManyToManyField(Works, null=True, blank=True)
    st = ((u'CT', u'Contest'),
          (u'MD', u'Moderate'),
          (u'VT', u'Vote'),
          (u'CM', u'Completed'),)
    stage = models.CharField(max_length=2, choices=st)
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