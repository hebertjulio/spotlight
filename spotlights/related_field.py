from rest_framework import serializers


class PageSlugField(serializers.RelatedField):
    def to_representation(self, value):
        return value.slug


class PanelSlugField(serializers.RelatedField):
    def to_representation(self, value):
        return value.slug


class LayoutSlugField(serializers.RelatedField):
    def to_representation(self, value):
        return value.slug
