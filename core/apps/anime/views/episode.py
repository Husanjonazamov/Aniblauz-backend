from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import EpisodeModel, AnimeModel
from ..serializers.episode import CreateEpisodeSerializer, ListEpisodeSerializer, RetrieveEpisodeSerializer


from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action




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

    @action(detail=False, methods=['get'], url_path='anime/(?P<anime_id>[^/.]+)')
    def list_by_anime(self, request, anime_id=None):
        anime = get_object_or_404(AnimeModel, id=anime_id)
        episodes = EpisodeModel.objects.filter(anime=anime)
        serializer = ListEpisodeSerializer(episodes, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RetrieveEpisodeSerializer
        return super().get_serializer_class()