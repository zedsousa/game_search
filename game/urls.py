from rest_framework.routers import DefaultRouter
from django.urls import include, path
from game import views

router  = DefaultRouter()

router.register("game_list", views.GameViewSet)
urlpatterns = [
    path("", include(router.urls)),
]