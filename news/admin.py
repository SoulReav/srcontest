from django.contrib import admin
from srcontest.news.models import News, Categories

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'dateCreated','publish' ,'author')
    date_hierarchy = 'dateCreated'

admin.site.register(Categories)

admin.site.register(News, NewsAdmin)

