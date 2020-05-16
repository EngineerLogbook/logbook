# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Team, Project


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'date_created',
        'published',
        'reviewed',
        'description',
        'token',
    )
    list_filter = ('date_created', 'published', 'reviewed')
    raw_id_fields = ('members',)
    search_fields = ('slug',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'date_created',
        'published',
        'reviewed',
        'team',
        'access_token',
        'description',
        'image',
        'logo',
    )
    list_filter = ('date_created', 'published', 'reviewed', 'team')
    search_fields = ('slug',)
