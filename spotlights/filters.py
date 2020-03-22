from django_filters import FilterSet, NumberFilter

from .models import News


class NewsFilterSet(FilterSet):
    section__isnull = NumberFilter(field_name='section', lookup_expr='isnull')

    class Meta:
        model = News
        fields = [
            'section__slug', 'section__isnull',
            'site__slug', 'editorial__slug',
        ]
