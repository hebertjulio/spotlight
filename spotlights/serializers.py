from rest_framework import serializers

from .models import Site, Section, Editorial, News, RelatedNews


class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        exclude = [
            'id', 'created', 'modified'
        ]


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        exclude = [
            'id', 'site', 'created', 'modified'
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


class NewsSerializer(serializers.ModelSerializer):

    site = SiteSerializer()
    editorials = EditorialSerializer(many=True)
    section = SectionSerializer()
    related_news = RelatedNewsSerializer(many=True)

    class Meta:
        model = News
        fields = '__all__'
