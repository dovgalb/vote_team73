from django.contrib import admin
from .models import Voting, Character, VotingCharacter
import openpyxl
from django.http import HttpResponse





@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age',)


@admin.register(VotingCharacter)
class VotingCharactersAdmin(admin.ModelAdmin):
    list_display = ('id', 'voting', 'character', 'num_of_votes')


class VotingCharacterInline(admin.TabularInline):
    model = Voting.characters.through
    extra = 1


class VotingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'is_active')
    filter_horizontal = ('characters',)
    inlines = (VotingCharacterInline,)


admin.site.register(Voting, VotingAdmin)
