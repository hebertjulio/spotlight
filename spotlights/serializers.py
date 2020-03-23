from rest_framework import serializers

from .models import Site, Panel, Layout, Tag, News, RelatedNews


class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        exclude = [
            'id', 'created', 'modified'
        ]


class PanelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Panel
        exclude = [
            'id', 'site', 'created', 'modified'
        ]


class LayoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Layout
        exclude = [
            'id', 'site', 'created', 'modified'
        ]


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        exclude = [
            'id', 'site', 'created', 'modified'
        ]


class RelatedNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RelatedNews
        exclude = [
            'id', 'news', 'created', 'modified'
        ]


class NewsSerializer(serializers.ModelSerializer):

    site = SiteSerializer()
    tags = TagSerializer(many=True)
    panel = PanelSerializer()
    layout = LayoutSerializer()
    related_news = RelatedNewsSerializer(many=True)

    class Meta:
        model = News
        fields = '__all__'
