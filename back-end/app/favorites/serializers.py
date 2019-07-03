""" Serializers for Favorites app. """
from rest_framework import serializers

from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    """
    Favorites Model serializer.
    """
    class Meta:
        model = Favorite
        fields = ('id', 'title',)