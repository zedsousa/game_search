from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.Serializer):
    gameName = serializers.CharField()
    gameID0 = serializers.CharField()
    gameID1 = serializers.CharField()
    gameID2 = serializers.CharField()
    gameID3 = serializers.CharField()
    amiiboUsage = serializers.CharField()
    amiiboUsagewrite = serializers.BooleanField()

    class Meta:
        model = Game
        fields = "__all__"
 
    