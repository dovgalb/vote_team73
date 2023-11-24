from django.contrib import admin
from .models import Voting, Vote
import openpyxl
from django.http import HttpResponse


@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'is_active')
    filter_horizontal = ('characters',)

    def export_votes_to_xlsx(self, request, queryset):
        # Создаем новый Excel-документ
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Voting Results"

        # Заголовки столбцов
        ws.append(["Candidate", "Votes"])

        # Получаем результаты голосования
        for voting in queryset:
            results = voting.winner  # предполагая, что get_voting_results возвращает список результатов для данного голосования

            # Добавляем результаты в документ
            ws.append([results['candidate']])

        # Сохраняем документ во временный файл
        temp_file_path = "/tmp/voting_results.xlsx"  # Путь к временному файлу
        wb.save(temp_file_path)

        # Возвращаем файл в HTTP Response
        with open(temp_file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="voting_results.xlsx"'

        return response

    export_votes_to_xlsx.short_description = "Export Voting Results to XLSX"

    actions = [export_votes_to_xlsx]

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'character', 'voting')

