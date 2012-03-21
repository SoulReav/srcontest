from django.contrib import admin
from grelka.news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date','public' ,'author')
    date_hierarchy = 'date'

admin.site.register(News, NewsAdmin)

