from django.db import models

# Create your models here.
class Game(models.Model):
    gameName = models.CharField(max_length=256)
    gameID0 = models.CharField(max_length=256)
    gameID1 = models.CharField(max_length=256)
    gameID2 = models.CharField(max_length=256)
    gameID3 = models.CharField(max_length=256)
    amiiboUsage = models.CharField(max_length=256)
    amiiboUsagewrite = models.BooleanField()
    
    def __str__(self):
        return self.name
    