from dal import autocomplete
from rest_framework.generics import ListAPIView

from .models import Panel, Page, Layout, Editorial, News
from .serializers import NewsSerializer
from .filters_sets import NewsFilterSet
from .services import get_current_news_id


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
        site_id = self.forwarded.get('site')
        if site_id:
            qs = Panel.objects.filter(site__id=site_id)
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
        page_id = self.forwarded.get('page')
        if page_id:
            qs = Editorial.objects.filter(page__id=page_id)
        return qs


class SupersedeAutocompleteView(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = News.objects.none()
        panel_id = self.forwarded.get('panel')
        if panel_id:
            qs = News.objects.filter(panel__id=panel_id)
        current_news_id = get_current_news_id(self.request)
        if current_news_id:
            qs = qs.exclude(id=current_news_id)
        return qs


class NewsListView(ListAPIView):

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filterset_class = NewsFilterSet
