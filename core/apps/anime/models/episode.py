from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.anime.models.anime import AnimeModel

import secrets
import string

def generate_random_id():
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(8))

class EpisodeModel(AbstractBaseModel):
    id = models.CharField(primary_key=True, max_length=8, default=generate_random_id, editable=False)
    name = models.CharField(_("name"), max_length=255)
    anime = models.ForeignKey(AnimeModel, related_name="episodes", on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(_("description"))
    episode_id = models.CharField(_("episode"), max_length=255)
    link = models.URLField(_("link"), max_length=500, blank=True, null=True, editable=False)  # Faqat ko'rish uchun


    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "episode"
        verbose_name = _("Anime qismlari")
        verbose_name_plural = _("Anime qismlari")
