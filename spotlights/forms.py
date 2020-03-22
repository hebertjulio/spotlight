from django import forms
from django.utils.translation import gettext_lazy as _
from django.db import transaction

from dal import autocomplete

from .models import Layout, News


class LayoutForm(forms.ModelForm):

    class Meta:
        model = Layout
        fields = [
            'site', 'section', 'name', 'slug',
        ]
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

    @transaction.atomic
    def save(self, commit=True):
        override = self.data.get('override')
        if override:
            try:
                obj = News.objects.get(pk=override)
                obj.section = None
                obj.save()
            except News.DoesNotExist:
                pass
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance

    class Meta:
        model = News
        fields = [
            'site', 'headline', 'blurb', 'editorial', 'url', 'image',
            'section', 'layout', 'override',
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
