from rest_framework import serializers

from .models import (
    Site, Editorial, News, NewsPage, RelatedNews
)
from .related_field import (
    PageSlugField, PanelSlugField, LayoutSlugField
)


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        exclude = [
            'id', 'created', 'modified'
        ]
        read_only_fields = [
            f.name for f in Site._meta.get_fields()]


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        exclude = [
            'id', 'site', 'created', 'modified'
        ]
        read_only_fields = [
            f.name for f in Site._meta.get_fields()]


class RelatedNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedNews
        exclude = [
            'id', 'news', 'created', 'modified'
        ]
        read_only_fields = [
            f.name for f in Site._meta.get_fields()]


class NewsPageSerializer(serializers.ModelSerializer):

    page = PageSlugField(read_only=True)
    panel = PanelSlugField(read_only=True)
    layout = LayoutSlugField(read_only=True)

    class Meta:
        model = NewsPage
        exclude = [
            'id', 'news', 'created', 'modified'
        ]
        read_only_fields = [
            f.name for f in Site._meta.get_fields()]


class NewsSerializer(serializers.ModelSerializer):

    site = SiteSerializer()
    editorials = EditorialSerializer(many=True)
    related_news = RelatedNewsSerializer(many=True)
    news_pages = NewsPageSerializer(many=True)

    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = [
            f.name for f in Site._meta.get_fields()]
