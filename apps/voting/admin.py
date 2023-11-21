from django.contrib import admin
from .models import Voting, Vote


@admin.register(Voting)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_active')
    filter_horizontal = ('characters',)


admin.site.register(Vote)
