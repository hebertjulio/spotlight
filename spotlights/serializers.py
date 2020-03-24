from rest_framework import serializers

from .models import (
    Site, Page, Panel, Layout, Editorial, News, NewsPage, RelatedNews)


class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        exclude = [
            'id', 'created', 'modified'
        ]


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        exclude = [
            'id', 'site', 'created', 'modified'
        ]


class PanelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Panel
        exclude = [
            'id', 'site', 'page', 'created', 'modified'
        ]


class LayoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Layout
        exclude = [
            'id', 'site', 'page', 'panel', 'created',
            'modified'
        ]


class EditorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Editorial
        exclude = [
            'id', 'site', 'created', 'modified'
        ]


class RelatedNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RelatedNews
        exclude = [
            'id', 'news', 'created', 'modified'
        ]


class NewsPageSerializer(serializers.ModelSerializer):

    page = PageSerializer()
    panel = PanelSerializer()
    layout = LayoutSerializer()

    class Meta:
        model = NewsPage
        exclude = [
            'id', 'news', 'created', 'modified'
        ]


class NewsSerializer(serializers.ModelSerializer):

    site = SiteSerializer()
    editorials = EditorialSerializer(many=True)
    related_news = RelatedNewsSerializer(many=True)
    news_pages = NewsPageSerializer(many=True)

    class Meta:
        model = News
        fields = '__all__'
