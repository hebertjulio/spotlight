from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.db import transaction

from imagekit.admin import AdminThumbnail

from .models import Site, Panel, Layout, Page, Editorial, News, RelatedNews
from .forms import PageForm, LayoutForm, NewsForm


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


@admin.register(Panel)
class PanelAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'slots', 'site',
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
        'name', 'slug', 'panel', 'site'
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
        'site', 'panel',
    ]
    exclude = [
        'created', 'modified',
    ]

    def get_queryset(self, request):
        sites = request.user.sites.all()
        qs = super().get_queryset(request)
        qs = qs.filter(site__in=sites)
        return qs


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):

    form = PageForm

    list_display = [
        'name', 'slug', 'site'
    ]
    search_fields = [
        'name', 'slug', 'editorials__name',
        'editorials__slug'
    ]
    autocomplete_fields = [
        'site',
    ]
    prepopulated_fields = {
        'slug': ['name']
    }
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

    exclude = [
        'created', 'modified', 'site',
    ]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    form = NewsForm
    empty_value_display = _('None')

    thumbnail = AdminThumbnail(image_field='thumbnail')
    thumbnail.short_description = _('thumbnail')

    list_display = [
        'site', 'headline', 'page', 'panel', 'layout'
    ]
    search_fields = [
        'headline', 'blurb', 'url', 'editorials__name',
        'editorials__slug',
    ]
    autocomplete_fields = [
        'site',
    ]
    list_filter = [
        'site', 'panel',
    ]
    inlines = [
        RelatedNewsInline,
    ]
    readonly_fields = [
        'thumbnail'
    ]

    @transaction.atomic()
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        supersede = request.POST.get('supersede')
        if supersede:
            try:
                supersede = News.objects.get(pk=supersede)
                supersede.panel = None
                supersede.save()
            except News.DoesNotExist:
                obj.supersede = None
                obj.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.request = request
        return form

    def get_queryset(self, request):
        sites = request.user.sites.all()
        qs = super().get_queryset(request)
        qs = qs.filter(site__in=sites)
        return qs
