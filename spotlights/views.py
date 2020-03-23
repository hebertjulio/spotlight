from dal import autocomplete
from rest_framework.generics import ListAPIView

from .models import Panel, Layout, Tag, News
from .serializers import NewsSerializer
from .filters_sets import NewsFilterSet
from .services import get_current_news_id


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


class TagAutocompleteView(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Tag.objects.none()
        site_id = self.forwarded.get('site')
        if site_id:
            qs = Tag.objects.filter(site__id=site_id)
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
