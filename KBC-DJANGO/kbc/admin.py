from django.contrib import admin
from .models import Player, Question, FFFResult, GameHistory

admin.site.register(Player)
admin.site.register(Question)
admin.site.register(FFFResult)
admin.site.register(GameHistory)