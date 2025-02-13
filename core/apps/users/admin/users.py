from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import UserModel


@admin.register(UserModel)
class UserAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
