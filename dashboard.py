# -*- coding: utf-8 -*-

from admin_tools.dashboard import modules, Dashboard

class CustomIndexDashboard(Dashboard):

    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)

        self.children.append(
            modules.ModelList( title = u'Пользователи', models=('django.contrib.auth.*',)),
        )

        try:
            self.children.append(
                modules.ModelList( title = u'Новости', models=('news.models.news','news.models.categories'))
            )
        except:
            print 'Ня!'



