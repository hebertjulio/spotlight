import re

from dal import autocomplete
from rest_framework.generics import ListAPIView

from .models import Section, Layout, Editorial, News
from .serializers import NewsSerializer
from .filters_sets import NewsFilterSet


class SectionAutocompleteView(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Section.objects.none()
        site_id = self.forwarded.get('site')
        if site_id:
            qs = Section.objects.filter(site__id=site_id)
        return qs


class LayoutAutocompleteView(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Layout.objects.none()
        section_id = self.forwarded.get('section')
        if section_id:
            qs = Layout.objects.filter(section__id=section_id)
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
        section_id = self.forwarded.get('section')
        if section_id:
            qs = News.objects.filter(section__id=section_id)
        http_refer = self.request.META['HTTP_REFERER']
        regex = r'news\/(\d)\/change'
        matches = re.search(regex, http_refer, re.DOTALL)
        if matches:
            qs = qs.exclude(id=matches.group(1))
        return qs


class NewsListView(ListAPIView):

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filterset_class = NewsFilterSet
