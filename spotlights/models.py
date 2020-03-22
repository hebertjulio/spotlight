from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel


class Site(TimeStampedModel):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100, unique=True)
    url = models.URLField(_('url'), unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = 'sites'


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
        verbose_name = 'section'
        verbose_name_plural = 'sections'
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
        verbose_name = 'layout'
        verbose_name_plural = 'layouts'


class Editorial(TimeStampedModel):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'editorial'
        verbose_name_plural = 'editorials'
        unique_together = [
            ['site', 'slug']
        ]


class News(TimeStampedModel):
    headline = models.CharField(_('headline'), max_length=100)
    blurb = models.CharField(_('blurb'), max_length=100, blank=True)
    editorial = models.ForeignKey('Editorial', on_delete=models.CASCADE)
    url = models.URLField(_('url'))
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    section = models.ForeignKey(
        'Section', on_delete=models.CASCADE, null=True, blank=True)
    layout = models.ForeignKey(
        'Layout', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.headline

    def __repr__(self):
        return self.headline

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
        unique_together = [
            ['site', 'url']
        ]
