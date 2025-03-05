from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Anime"),
        "separator": True,  
        "items": [
            {
                "title": _("Anime Qismlari"),
                "icon": "play_arrow",
                "link": reverse_lazy("admin:anime_episodemodel_changelist"),
            },
            {
                "title": _("Animelar"),
                "icon": "movie",
                "link": reverse_lazy("admin:anime_animemodel_changelist"),
            },
            {
                "title": _("Foydalanuvchilar"),
                "icon": "person",
                "link": reverse_lazy("admin:users_usermodel_changelist"),
            },
        ],
    },
]
