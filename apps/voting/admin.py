from django.contrib import admin
from .models import Voting


@admin.register(Voting)
class ModelNameAdmin(admin.ModelAdmin):
    pass
