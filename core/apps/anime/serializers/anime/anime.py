from rest_framework import serializers

from ...models import AnimeModel


class BaseAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListAnimeSerializer(BaseAnimeSerializer):
    class Meta(BaseAnimeSerializer.Meta): ...


class RetrieveAnimeSerializer(BaseAnimeSerializer):
    class Meta(BaseAnimeSerializer.Meta): ...


class CreateAnimeSerializer(BaseAnimeSerializer):
    class Meta(BaseAnimeSerializer.Meta): ...
