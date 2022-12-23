from django.contrib import admin
from .models import Posting

class TheDevHubAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'posted', 'url', 'note')

# Register your models here.

admin.site.register(Posting, TheDevHubAdmin)