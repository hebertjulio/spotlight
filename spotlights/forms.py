from django import forms
from django.utils.translation import gettext_lazy as _
from django.db import transaction

from dal import autocomplete

from .models import Panel, Layout, News, NewsPage
from .services import get_current_news


class PanelForm(forms.ModelForm):

    class Media:
        js = ('js/panelform.js',)

    class Meta:
        model = Panel
        fields = '__all__'
        widgets = {
            'page': autocomplete.ModelSelect2(
                url='spotlights:page_autocomplete',
                forward=['site']
            ),
        }


class LayoutForm(forms.ModelForm):

    class Media:
        js = ('js/layoutform.js',)

    class Meta:
        model = Layout
        fields = '__all__'
        widgets = {
            'page': autocomplete.ModelSelect2(
                url='spotlights:page_autocomplete',
                forward=['site']
            ),
            'panel': autocomplete.ModelSelect2(
                url='spotlights:panel_autocomplete',
                forward=['page']
            ),
        }


class NewsPageForm(forms.ModelForm):

    supersede = forms.ModelChoiceField(
        queryset=News.objects.all(), required=False,
        widget=autocomplete.ModelSelect2(
            url='spotlights:supersede_autocomplete', forward=['panel']
        ),
        label=_('Supersede'),
    )

    panel_set = 0

    def clean_panel(self):
        panel = self.cleaned_data['panel']
        if panel:
            qs = NewsPage.objects.filter(panel=panel)
            supersede = self.data.get(
                'newspage_set-%d-supersede' % NewsPageForm.panel_set)
            current = get_current_news(self.request)
            ids = [i for i in [supersede, current] if i]
            if any(ids):
                qs = qs.exclude(news_id__in=ids)
            if qs.count() >= panel.slots:
                raise forms.ValidationError(
                    _('Panel full, max news count %d.' % panel.slots))
        NewsPageForm.panel_set += 1
        return panel

    @transaction.atomic()
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            count = self.data.get('newspage_set-INITIAL_FORMS')
            for i in range(int(count)):
                supersede = self.data.get(
                    'newspage_set-%d-supersede' % i)
                if supersede:
                    try:
                        obj = NewsPage.objects.get(
                            news_id=supersede, panel=instance.panel)
                        obj.panel = obj.layout = None
                        obj.save()
                    except NewsPage.DoesNotExist:
                        pass
        return instance

    class Media:
        js = ('js/newspageform.js',)

    class Meta:
        model = NewsPage
        fields = '__all__'
        widgets = {
            'page': autocomplete.ModelSelect2(
                url='spotlights:page_autocomplete',
                forward=['site']
            ),
            'panel': autocomplete.ModelSelect2(
                url='spotlights:panel_autocomplete',
                forward=['page']
            ),
            'layout': autocomplete.ModelSelect2(
                url='spotlights:layout_autocomplete',
                forward=['panel']
            ),
        }


class NewsForm(forms.ModelForm):

    class Media:
        js = ('js/newsform.js',)

    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'editorials': autocomplete.ModelSelect2Multiple(
                url='spotlights:editorial_autocomplete',
                forward=['site']
            ),
        }
