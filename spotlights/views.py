from dal import autocomplete
from rest_framework.generics import ListAPIView

from .models import Page, Panel, Layout, Editorial, News
from .serializers import NewsSerializer
from .filters_sets import NewsFilterSet
from .services import get_current_news


class PageAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Page.objects.none()
        site_id = self.forwarded.get('site')
        if site_id:
            qs = Page.objects.filter(site__id=site_id)
        return qs


class PanelAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Panel.objects.none()
        page_id = self.forwarded.get('page')
        if page_id:
            qs = Panel.objects.filter(page__id=page_id)
        return qs


class LayoutAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Layout.objects.none()
        panel_id = self.forwarded.get('panel')
        if panel_id:
            qs = Layout.objects.filter(panel__id=panel_id)
        return qs


class EditorialAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Editorial.objects.none()
        site_id = self.forwarded.get('site')
        if site_id:
            qs = Editorial.objects.filter(site__id=site_id)
        return qs


class SupersedeAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = News.objects.none()
        panel_id = self.forwarded.get('panel')
        if panel_id:
            qs = News.objects.filter(newspage__panel__id=panel_id)
        current = get_current_news(self.request)
        if current:
            qs = qs.exclude(id=current)
        return qs


class NewsListView(ListAPIView):
    queryset = News.objects.select_related().all()
    serializer_class = NewsSerializer
    filterset_class = NewsFilterSet
