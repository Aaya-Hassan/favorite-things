from rest_framework import viewsets

from .models import Favorite
from .serializers import FavoriteSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    """
    Favorite API view set.
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
