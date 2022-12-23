from django.contrib import admin
from .models import Posting, Application, Note

# Register your models here.

admin.site.register(Posting)
admin.site.register(Application)
admin.site.register(Note)