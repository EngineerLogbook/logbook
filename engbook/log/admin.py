from django.contrib import admin
from .models import Logger, LogFile, LogURL
# Register your models here.
admin.site.register(Logger)
admin.site.register(LogFile)
admin.site.register(LogURL)
