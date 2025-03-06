from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from ..models import AnimeModel, EpisodeModel


class EpisodeInline(TabularInline):
    model = EpisodeModel
    extra = 1 


@admin.register(AnimeModel)
class AnimeAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
    inlines = [EpisodeInline]
    readonly_fields = ('link',)
