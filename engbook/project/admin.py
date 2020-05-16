# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Team, Project


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    exclude = (
        'slug',
        'date_created',
        'published',
        'reviewed',
        
    )
    list_display = (

        'title',
        'description',
        'date_created',

        'id',
        'slug',
        'published',
        'reviewed',
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
