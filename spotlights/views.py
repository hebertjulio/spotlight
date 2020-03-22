from dal import autocomplete

from .models import Section, Layout, Editorial, News


class SectionAutocompleteView(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        site_id = self.forwarded.get('site')
        qs = Section.objects.none()
        if site_id:
            qs = Section.objects.filter(site__id=site_id)
        return qs


class LayoutAutocompleteView(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        section_id = self.forwarded.get('section')
        qs = Layout.objects.none()
        if section_id:
            qs = Layout.objects.filter(section__id=section_id)
        return qs


class EditorialAutocompleteView(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        site_id = self.forwarded.get('site')
        qs = Editorial.objects.none()
        if site_id:
            qs = Editorial.objects.filter(site__id=site_id)
        return qs


class NewsAutocompleteView(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        section_id = self.forwarded.get('section')
        qs = News.objects.none()
        if section_id:
            qs = News.objects.filter(section__id=section_id)
        return qs
