from django_filters import FilterSet, NumberFilter

from .models import News


class NewsFilterSet(FilterSet):
    panel__isnull = NumberFilter(field_name='panel', lookup_expr='isnull')

    class Meta:
        model = News
        fields = [
            'panel__slug', 'panel__isnull',
            'site__slug', 'editorials__slug',
        ]
