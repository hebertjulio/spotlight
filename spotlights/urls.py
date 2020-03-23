from django.urls import path

from .views import (
    SectionAutocompleteView, LayoutAutocompleteView, EditorialAutocompleteView,
    SupersedeAutocompleteView, NewsListView
)


app_name = 'spotlights'

urlpatterns = [
    path(
        'editorial/autocomplete/',
        EditorialAutocompleteView.as_view(),
        name='editorial_autocomplete',
    ),
    path(
        'section/autocomplete/',
        SectionAutocompleteView.as_view(),
        name='section_autocomplete',
    ),
    path(
        'layout/autocomplete/',
        LayoutAutocompleteView.as_view(),
        name='layout_autocomplete',
    ),
    path(
        'supersede/autocomplete/',
        SupersedeAutocompleteView.as_view(),
        name='supersede_autocomplete',
    ),
    path(
        'news/',
        NewsListView.as_view(),
        name='news_list',
    ),
]
