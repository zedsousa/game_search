from django.http import HttpResponse
from django.shortcuts import render
from .models import Game
from .serializers import GameSerializer

from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import viewsets


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = "__all__"
