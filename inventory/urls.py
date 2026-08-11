from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EquipoViewSet, health, version


router = DefaultRouter()

router.register(
    r"equipos",
    EquipoViewSet,
    basename="equipos"
)


urlpatterns = [

    path("", include(router.urls)),

    path(
        "health/",
        health,
        name="health"
    ),

    path(
        "version/",
        version,
        name="version"
    ),
]
