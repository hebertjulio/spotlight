from django.urls import path

from .views import (
    SectionAutocompleteView, EditorialAutocompleteView
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
]
