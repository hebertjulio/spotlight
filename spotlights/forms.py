from django import forms
from django.utils.translation import gettext_lazy as _

from dal import autocomplete

from .models import Page, Layout, News
from .services import get_current_news_id


class PageForm(forms.ModelForm):

    class Media:
        js = ('js/custom.js',)

    class Meta:
        model = Page
        fields = '__all__'
        widgets = {
            'editorials': autocomplete.ModelSelect2Multiple(
                url='spotlights:editorial_autocomplete',
                forward=['site']
            ),
        }


class LayoutForm(forms.ModelForm):

    class Media:
        js = ('js/custom.js',)

    class Meta:
        model = Layout
        fields = '__all__'
        widgets = {
            'panel': autocomplete.ModelSelect2(
                url='spotlights:panel_autocomplete',
                forward=['site']
            ),
        }


class NewsForm(forms.ModelForm):

    supersede = forms.ModelChoiceField(
        queryset=News.objects.all(), required=False,
        widget=autocomplete.ModelSelect2(
            url='spotlights:supersede_autocomplete', forward=['panel', 'id']
        ),
        label=_('Supersede'),
    )

    def clean_panel(self):
        supersede = self.data.get('supersede')
        panel = self.cleaned_data['panel']
        if panel and not supersede:
            qs = News.objects.filter(panel=panel)
            current_news_id = get_current_news_id(self.request)
            if current_news_id:
                qs = qs.exclude(id=current_news_id)
            if qs.count() >= panel.slots:
                raise forms.ValidationError(
                    _('Panel full, max news count %d.' % panel.slots))
        return panel

    class Media:
        js = ('js/custom.js',)

    class Meta:
        model = News
        fields = [
            'headline', 'blurb', 'site', 'page', 'editorials',
            'panel', 'layout', 'supersede', 'url', 'image',
        ]
        widgets = {
            'page': autocomplete.ModelSelect2(
                url='spotlights:page_autocomplete',
                forward=['site']
            ),
            'editorials': autocomplete.ModelSelect2Multiple(
                url='spotlights:editorial_autocomplete',
                forward=['page']
            ),
            'panel': autocomplete.ModelSelect2(
                url='spotlights:panel_autocomplete',
                forward=['site']
            ),
            'layout': autocomplete.ModelSelect2(
                url='spotlights:layout_autocomplete',
                forward=['panel']
            ),
        }
