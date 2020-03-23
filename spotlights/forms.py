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

    supersede = forms.ModelChoiceField(
        queryset=News.objects.all(), required=False,
        widget=autocomplete.ModelSelect2(
            url='spotlights:supersede_autocomplete', forward=['section', 'id']
        ),
        label=_('Supersede'),
    )

    def clean_section(self):
        supersede = self.data.get('supersede')
        section = self.cleaned_data['section']
        if section and not supersede:
            count = News.objects.filter(section=section).count()
            if count >= section.slots:
                raise forms.ValidationError(
                    _('Section full, max news count %d.' % section.slots))
        return section

    class Media:
        js = ('js/custom.js',)

    class Meta:
        model = News
        fields = [
            'site', 'headline', 'blurb', 'editorial', 'url',
            'section', 'layout', 'supersede', 'image'
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
