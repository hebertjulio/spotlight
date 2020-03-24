from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.db import transaction
from django.forms.models import BaseInlineFormSet

from imagekit.admin import AdminThumbnail

from .models import (
    Site, Page, Panel, Layout, Editorial, News, RelatedNews, NewsPage
)
from .forms import PanelForm, LayoutForm, NewsForm, NewsPageForm


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
    exclude = [
        'created', 'modified',
    ]

    @transaction.atomic()
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            request.user.sites.add(obj)

    def get_queryset(self, request):
        return request.user.sites.all()


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'site',
    ]
    search_fields = [
        'name', 'slug'
    ]
    prepopulated_fields = {
        'slug': ['name']
    }
    autocomplete_fields = [
        'site',
    ]
    list_filter = [
        'site',
    ]
    exclude = [
        'created', 'modified',
    ]

    def get_queryset(self, request):
        sites = request.user.sites.all()
        qs = super().get_queryset(request)
        qs = qs.filter(site__in=sites)
        return qs


@admin.register(Panel)
class PanelAdmin(admin.ModelAdmin):

    form = PanelForm

    list_display = [
        'name', 'slug', 'slots', 'site', 'page',
    ]
    search_fields = [
        'name', 'slug'
    ]
    prepopulated_fields = {
        'slug': ['name']
    }
    autocomplete_fields = [
        'site',
    ]
    list_filter = [
        'site',
    ]
    exclude = [
        'created', 'modified',
    ]


@admin.register(Layout)
class LayoutAdmin(admin.ModelAdmin):

    form = LayoutForm

    list_display = [
        'name', 'slug', 'site', 'page', 'panel',
    ]
    search_fields = [
        'name', 'slug'
    ]
    autocomplete_fields = [
        'site',
    ]
    prepopulated_fields = {
        'slug': ['name']
    }
    list_filter = [
        'site', 'page',
    ]
    exclude = [
        'created', 'modified',
    ]

    def get_queryset(self, request):
        sites = request.user.sites.all()
        qs = super().get_queryset(request)
        qs = qs.filter(site__in=sites)
        return qs


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
    autocomplete_fields = [
        'site',
    ]
    list_filter = [
        'site',
    ]
    exclude = [
        'created', 'modified',
    ]

    def get_queryset(self, request):
        sites = request.user.sites.all()
        qs = super().get_queryset(request)
        qs = qs.filter(site__in=sites)
        return qs


class RelatedNewsInline(admin.TabularInline):

    model = RelatedNews
    min_num = 0
    max_num = 3
    extra = 1


class NewsPageFormset(BaseInlineFormSet):

    def _construct_form(self, i, **kwargs):
        form = super()._construct_form(i, **kwargs)
        form.request = self.request
        return form


class NewsPageInline(admin.TabularInline):

    form = NewsPageForm
    model = NewsPage
    formset = NewsPageFormset
    min_num = 1
    max_num = 3
    extra = 0

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.request = request
        return formset


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    form = NewsForm
    empty_value_display = _('None')

    thumbnail = AdminThumbnail(image_field='thumbnail')
    thumbnail.short_description = _('thumbnail')

    list_display = [
        'headline', 'site',
    ]
    search_fields = [
        'headline', 'blurb', 'url', 'editorials__name',
        'editorials__slug',
    ]
    autocomplete_fields = [
        'site',
    ]
    list_filter = [
        'site',
    ]
    inlines = [
        RelatedNewsInline,
        NewsPageInline
    ]
    readonly_fields = [
        'thumbnail'
    ]
    exclude = [
        'created', 'modified',
    ]

    def get_queryset(self, request):
        sites = request.user.sites.all()
        qs = super().get_queryset(request)
        qs = qs.filter(site__in=sites)
        return qs
