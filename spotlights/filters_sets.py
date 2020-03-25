from django_filters import FilterSet, NumberFilter

from .models import News


class NewsFilterSet(FilterSet):
    newspage__panel__isnull = NumberFilter(
        field_name='newspage__panel', lookup_expr='isnull')

    class Meta:
        model = News
        fields = [
            'newspage__panel__slug', 'newspage__panel__isnull',
            'site__slug', 'editorials__slug', 'newspage__page__slug'
        ]
