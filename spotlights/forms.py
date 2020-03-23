from django import forms
from django.utils.translation import gettext_lazy as _

from dal import autocomplete

from .models import Layout, News


class LayoutForm(forms.ModelForm):

    class Media:
        js = ('js/custom.js',)

    class Meta:
        model = Layout
        fields = '__all__'
        widgets = {
            'section': autocomplete.ModelSelect2(
                url='spotlights:section_autocomplete',
                forward=['site']
            ),
        }


class NewsForm(forms.ModelForm):

    override = forms.ModelChoiceField(
        queryset=News.objects.all(), required=False,
        widget=autocomplete.ModelSelect2(
            url='spotlights:news_autocomplete', forward=['section']
        ),
        label=_('Override'),
    )

    def clean_section(self):
        section = self.cleaned_data['section']
        if section and (not self.instance or not self.instance.id):
            qs = News.objects.filter(section=section)
            override = self.data.get('override')
            if override:
                qs = qs.exclude(id=override)
            if qs.count() >= section.slots:
                raise forms.ValidationError(
                    _('Section full, max news count %d.' % section.slots))
        return section

    class Media:
        js = ('js/custom.js',)

    class Meta:
        model = News
        fields = [
            'site', 'headline', 'blurb', 'editorial', 'url',
            'section', 'layout', 'override', 'image'
        ]
        widgets = {
            'editorial': autocomplete.ModelSelect2(
                url='spotlights:editorial_autocomplete',
                forward=['site']
            ),
            'section': autocomplete.ModelSelect2(
                url='spotlights:section_autocomplete',
                forward=['site']
            ),
            'layout': autocomplete.ModelSelect2(
                url='spotlights:layout_autocomplete',
                forward=['section']
            ),
        }
