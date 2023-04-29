"""
Serializers for recipe
"""

from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """ Serializer for recipe """

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """ serializer for recipe details """

    class Meta(RecipeSerializer.Meta):
        filds = RecipeSerializer.Meta.fields + ['description']
