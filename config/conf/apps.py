from config.env import env

APPS = [
    "channels",
    "cacheops",
    "rosetta",
    "django_ckeditor_5",
    "modeltranslation",
    "parler",
    "drf_spectacular",
    "rest_framework",
    "corsheaders",
    "django_filters",
    "django_redis",
    "rest_framework_simplejwt",
    "django_core",
    "core.apps.accounts.apps.AccountsConfig",
    
    # install apps
    'core.apps.users',
    'core.apps.anime',
    'core.apps.api',
]

if env.str("PROJECT_ENV") == "debug":
    APPS += [
        "silk",
    ]