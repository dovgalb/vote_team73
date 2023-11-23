from django.contrib import admin
from .models import Characters


@admin.register(Characters)
class CharactersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
