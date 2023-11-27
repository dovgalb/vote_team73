from django.contrib import admin
from .models import Voting, Character, VotingCharacters
import openpyxl
from django.http import HttpResponse


@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'is_active')
    filter_horizontal = ('characters',)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age',)


@admin.register(VotingCharacters)
class VotingCharactersAdmin(admin.ModelAdmin):
    list_display = ('id', 'voting', 'character', 'num_of_votes')


