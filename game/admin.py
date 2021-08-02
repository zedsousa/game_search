from django.contrib import admin
from .models import Game

class ListGame(admin.ModelAdmin):
    list_display = ('gameName','amiiboUsage', 'amiiboUsagewrite',)
    list_display_links = ('gameName',)
    search_fields = ('gameName',)
    list_filter = ('amiiboUsagewrite',)
    list_per_page = 10

admin.site.register(Game, ListGame)