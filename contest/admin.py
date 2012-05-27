from django.contrib import admin
from contest.models import Contest, Terms, Extra, Works

class ExtraInline(admin.TabularInline):
    model = Extra

class TermsInline(admin.TabularInline):
    model = Terms

class ContestAdmin(admin.ModelAdmin):
    inlines = [
        TermsInline, ExtraInline,
        ]

class TermsAdmin(admin.ModelAdmin):
    pass

class ExtraAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contest, ContestAdmin)
admin.site.register(Terms, TermsAdmin)
admin.site.register(Extra,ExtraAdmin)
admin.site.register(Works)
