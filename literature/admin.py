from django.contrib import admin
from .models import Maestro, Work, Text, Part, Essay, UserLibrary

admin.site.register(Maestro)
admin.site.register(Work)
admin.site.register(Text)
admin.site.register(Part)
admin.site.register(Essay)
admin.site.register(UserLibrary)
