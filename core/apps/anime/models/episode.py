from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.anime.models.anime import AnimeModel


class EpisodeModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    anime = models.ForeignKey(AnimeModel, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(_("description"))
    episode_id = models.CharField(_("episode"), max_length=255)
    

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
