from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel


class Site(TimeStampedModel):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100, unique=True)
    url = models.URLField(_('url'), unique=True)

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = 'sites'


class Section(TimeStampedModel):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100, unique=True)
    slots = models.PositiveSmallIntegerField(
        _('slots'), validators=[MinValueValidator(1)])
    site = models.ForeignKey('Site', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'section'
        verbose_name_plural = 'sections'
        unique_together = [
            ['site', 'slug']
        ]


class Editorial(TimeStampedModel):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'editorial'
        verbose_name_plural = 'editorials'
        unique_together = [
            ['site', 'slug']
        ]


class News(TimeStampedModel):
    headline = models.CharField(_('title'), max_length=100)
    blurb = models.CharField(_('blurb'), max_length=100)
    editorial = models.ForeignKey('Editorial', on_delete=models.CASCADE)
    url = models.URLField(_('url'))
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
        unique_together = [
            ['site', 'url']
        ]
