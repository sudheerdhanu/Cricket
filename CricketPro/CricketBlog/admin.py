from django.contrib import admin

from .models import Player_history,Player,Match,Team,Score

admin.site.register(Player_history)
admin.site.register(Player)

admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Score)
