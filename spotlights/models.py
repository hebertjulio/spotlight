from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel

from imagekit.processors import ResizeToFit
from imagekit.models import ImageSpecField


class Site(TimeStampedModel):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100, unique=True)
    url = models.URLField(_('url'), unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = _('site')
        verbose_name_plural = _('sites')


class Section(TimeStampedModel):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100, unique=True)
    slots = models.PositiveSmallIntegerField(
        _('slots'), validators=[MinValueValidator(1)])
    site = models.ForeignKey('Site', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = _('section')
        verbose_name_plural = _('sections')
        unique_together = [
            ['site', 'slug']
        ]


class Layout(TimeStampedModel):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100, unique=True)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = _('layout')
        verbose_name_plural = _('layouts')


class Editorial(TimeStampedModel):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = _('editorial')
        verbose_name_plural = _('editorials')
        unique_together = [
            ['site', 'slug']
        ]


class News(TimeStampedModel):
    headline = models.CharField(_('headline'), max_length=100)
    blurb = models.CharField(_('blurb'), max_length=100, blank=True)
    editorial = models.ForeignKey('Editorial', on_delete=models.CASCADE)
    url = models.URLField(_('url'))
    image = models.ImageField(_('image'), upload_to='news', blank=True)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    section = models.ForeignKey(
        'Section', on_delete=models.CASCADE, null=True, blank=True)
    layout = models.ForeignKey(
        'Layout', on_delete=models.CASCADE, null=True, blank=True)

    thumbnail = ImageSpecField(
        source='image', processors=[ResizeToFit(300, 300)],
        format='JPEG', options={'quality': 60}
    )

    @property
    def related_news(self):
        return self.relatednews_set.all()

    def __str__(self):
        return self.headline

    def __repr__(self):
        return self.headline

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')
        unique_together = [
            ['site', 'url']
        ]
        ordering = [
            '-created',
        ]


class RelatedNews(TimeStampedModel):

    headline = models.CharField(_('headline'), max_length=100)
    url = models.URLField(_('url'))
    news = models.ForeignKey('News', on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    def __repr__(self):
        return self.headline

    class Meta:
        verbose_name = _('related news')
        verbose_name_plural = _('related news')
