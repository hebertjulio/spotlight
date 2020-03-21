from dal import autocomplete

from .models import Section, Editorial


class SectionAutocompleteView(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        site_id = self.forwarded.get('site')
        qs = Section.objects.none()
        if site_id is not None:
            qs = Section.objects.filter(site__id=site_id)
        return qs


class EditorialAutocompleteView(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        site_id = self.forwarded.get('site')
        qs = Editorial.objects.none()
        if site_id is not None:
            qs = Editorial.objects.filter(site__id=site_id)
        return qs
