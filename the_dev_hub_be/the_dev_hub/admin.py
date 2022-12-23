from django.contrib import admin
from .models import Posting, Application, Note
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'posted', 'url', 'note')

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'applied', 'hiring_manager', 'compensation', 'work_site', 'location')

# Register your models here.

admin.site.register(Posting, JobAdmin)
admin.site.register(Application, ApplicationAdmin)