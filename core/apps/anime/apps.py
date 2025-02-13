from django.apps import AppConfig


class ModuleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.apps.anime"
    
    def ready(self):
        import core.apps.anime.signals.signals
