from django.urls import path

from .views import (
    PanelAutocompleteView, LayoutAutocompleteView, TagAutocompleteView,
    SupersedeAutocompleteView, NewsListView
)


app_name = 'spotlights'

urlpatterns = [
    path(
        'tag-autocomplete/',
        TagAutocompleteView.as_view(),
        name='tag_autocomplete',
    ),
    path(
        'panel-autocomplete/',
        PanelAutocompleteView.as_view(),
        name='panel_autocomplete',
    ),
    path(
        'layout-autocomplete/',
        LayoutAutocompleteView.as_view(),
        name='layout_autocomplete',
    ),
    path(
        'supersede-autocomplete/',
        SupersedeAutocompleteView.as_view(),
        name='supersede_autocomplete',
    ),
    path(
        'news/',
        NewsListView.as_view(),
        name='news_list',
    ),
]
