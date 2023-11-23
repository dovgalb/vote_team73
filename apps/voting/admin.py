from django.contrib import admin
from .models import Voting, Vote


@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'is_active')
    filter_horizontal = ('characters',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'character', 'voting')

