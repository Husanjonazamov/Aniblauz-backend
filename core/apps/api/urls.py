from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.apps.users.views import UserView
from core.apps.anime.views import AnimeView

router = DefaultRouter()

# anime url
router.register(r"anime", AnimeView, basename='anime')

# users url
router.register(r"users", UserView, basename='users')



urlpatterns = [
    path("", include(router.urls)),
]
