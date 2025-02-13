from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class UserModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    user_id = models.CharField(_("user_id"), max_length=50)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "user"
        verbose_name = _("UserModel")
        verbose_name_plural = _("UserModels")
