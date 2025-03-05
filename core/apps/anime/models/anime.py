from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
import uuid

import secrets
import string

def generate_random_id():
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(8))
    

class AnimeModel(AbstractBaseModel):
    id = models.CharField(primary_key=True, max_length=8, default=generate_random_id, editable=False)
    name = models.CharField(_("name"), max_length=255, null=True, blank=True)
    description = models.TextField(_("description"), null=True, blank=True)
    anime_id = models.CharField(_("anime"), max_length=255)
    link = models.URLField(_("link"), max_length=500, blank=True, null=True, editable=False)

    def __str__(self):
        return self.name
    
    
    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "anime"
        verbose_name = _("Animelar")
        verbose_name_plural = _("Animelar")
