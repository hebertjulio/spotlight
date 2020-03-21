from django import forms
from django.utils.translation import gettext_lazy as _

from .models import News


class NewsForm(forms.ModelForm):

    def clean_section(self):
        section = self.cleaned_data['section']
        count_news = News.objects.filter(section=section).count()
        if count_news >= section.slots:
            raise forms.ValidationError(
                _('Section full, max news count %d.' % section.slots))
        return section

    class Meta:
        model = News
        fields = '__all__'
