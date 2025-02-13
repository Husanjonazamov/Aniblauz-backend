from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import AnimeModel


@admin.register(AnimeModel)
class AnimeAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
