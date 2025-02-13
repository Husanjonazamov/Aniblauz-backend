from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import AnimeModel
from ..serializers.anime import CreateAnimeSerializer, ListAnimeSerializer, RetrieveAnimeSerializer


@extend_schema(tags=["anime"])
class AnimeView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = AnimeModel.objects.all()
    serializer_class = ListAnimeSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListAnimeSerializer,
        "retrieve": RetrieveAnimeSerializer,
        "create": CreateAnimeSerializer,
    }
