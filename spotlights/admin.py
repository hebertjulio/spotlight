from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from imagekit.admin import AdminThumbnail

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
    exclude = [
        'created', 'modified',
    ]

    def get_queryset(self, request):
        return request.user.sites.all()


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
        'name', 'slug', 'section', 'site'
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
    list_filter = [
        'site', 'section',
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
        'site', 'headline', 'editorial', 'section',
    ]
    search_fields = [
        'headline', 'blurb', 'url',
    ]
    autocomplete_fields = [
        'site',
    ]
    list_filter = [
        'site', 'section',
    ]
    inlines = [
        RelatedNewsInline,
    ]

    exclude = ['thumbnail']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.thumbnail and obj.thumbnail.url:
            self.readonly_fields = ['thumbnail']
            self.exclude = [f for f in self.exclude if f != 'thumbnail']
        return form

    def get_queryset(self, request):
        sites = request.user.sites.all()
        qs = super().get_queryset(request)
        qs = qs.filter(site__in=sites)
        return qs
