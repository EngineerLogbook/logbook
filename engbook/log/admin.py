# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Logger, LogFile, LogURL


@admin.register(Logger)
class LoggerAdmin(admin.ModelAdmin):
    exclude=('slug','published','reviewed', 'date_created','date_modified',)
    list_display = (
        'id',
        'title',
        'published',
        'reviewed',
        'note',
        'user',
        'project',
    )
    list_filter = (
        'date_created',
        'published',
        'reviewed',
        'user',
        'date_modified',
        'project',
    )
    search_fields = ('slug',)


@admin.register(LogFile)
class LogFileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'date_created',
        'published',
        'reviewed',
        'file',
        'filetype',
    )
    list_filter = ('date_created', 'published', 'reviewed')
    search_fields = ('slug',)


@admin.register(LogURL)
class LogURLAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'log')
    list_filter = ('log',)
