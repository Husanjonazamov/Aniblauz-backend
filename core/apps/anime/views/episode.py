from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import EpisodeModel
from ..serializers.episode import CreateEpisodeSerializer, ListEpisodeSerializer, RetrieveEpisodeSerializer


@extend_schema(tags=["episode"])
class EpisodeView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = EpisodeModel.objects.all()
    serializer_class = ListEpisodeSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListEpisodeSerializer,
        "retrieve": RetrieveEpisodeSerializer,
        "create": CreateEpisodeSerializer,
    }
