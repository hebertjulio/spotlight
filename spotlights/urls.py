from django.urls import path

from .views import (
    SectionAutocompleteView, EditorialAutocompleteView, NewsAutocompleteView
)


app_name = 'spotlights'

urlpatterns = [
    path(
        'editorial-autocomplete/',
        EditorialAutocompleteView.as_view(),
        name='editorial_autocomplete',
    ),
    path(
        'section-autocomplete/',
        SectionAutocompleteView.as_view(),
        name='section_autocomplete',
    ),
    path(
        'news-autocomplete/',
        NewsAutocompleteView.as_view(),
        name='news_autocomplete',
    ),
]
