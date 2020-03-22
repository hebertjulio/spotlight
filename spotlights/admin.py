from django.contrib import admin
from django.utils.translation import gettext_lazy as _


from .models import Site, Section, Layout, Editorial, News, RelatedNews
from .forms import LayoutForm, NewsForm


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


@admin.register(Layout)
class LayoutAdmin(admin.ModelAdmin):

    form = LayoutForm

    list_display = [
        'name', 'slug', 'section',
    ]
    search_fields = [
        'name', 'slug'
    ]
    autocomplete_fields = [
        'site', 'section',
    ]
    prepopulated_fields = {
        'slug': ['name']
    }
    readonly_fields = [
        'created', 'modified'
    ]
    list_filter = [
        'site', 'section',
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


class RelatedNewsInline(admin.TabularInline):

    model = RelatedNews
    min_num = 0
    max_num = 3


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    form = NewsForm
    empty_value_display = _('None')

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
        'site', 'editorial', 'section', 'layout'
    ]
    list_filter = [
        'site', 'section',
    ]
    inlines = [
        RelatedNewsInline,
    ]
