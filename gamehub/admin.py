from django.contrib import admin
from gamehub.models import Game, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'date', 'quality_rate', 'music_rate', 'community_rate')

class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Game, GameAdmin)
admin.site.register(Comment, CommentAdmin)

