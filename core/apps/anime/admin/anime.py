from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import AnimeModel, EpisodeModel


class EpisodeInline(admin.TabularInline):
    model = EpisodeModel
    extra = 1 


@admin.register(AnimeModel)
class AnimeAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
    inlines = [EpisodeInline]