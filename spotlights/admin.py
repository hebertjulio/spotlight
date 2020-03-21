from django.contrib import admin

from .models import Site, Section, Editorial, News


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'url',
    ]
    search_fields = [
        'name', 'slug'
    ]
    prepopulated_fields = {
        'slug': ['name']
    }
    readonly_fields = [
        'created', 'modified'
    ]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'slots', 'site',
    ]
    search_fields = [
        'name', 'slug'
    ]
    prepopulated_fields = {
        'slug': ['name']
    }
    readonly_fields = [
        'created', 'modified'
    ]
    autocomplete_fields = [
        'site',
    ]
    list_filter = [
        'site',
    ]


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'site',
    ]
    search_fields = [
        'name', 'slug'
    ]
    prepopulated_fields = {
        'slug': ['name']
    }
    readonly_fields = [
        'created', 'modified'
    ]
    autocomplete_fields = [
        'site',
    ]
    list_filter = [
        'site',
    ]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'site', 'headline', 'editorial', 'section',
    ]
    search_fields = [
        'headline', 'blurb', 'url',
    ]
    readonly_fields = [
        'created', 'modified'
    ]
    autocomplete_fields = [
        'site', 'editorial', 'section'
    ]
    list_filter = [
        'site', 'section',
    ]
