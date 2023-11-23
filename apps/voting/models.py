from django.db import models
from django.db.models import Count, F, Max
from django.utils import timezone

from apps.characters.models import Characters


class Voting(models.Model):
    """
    Модель предназначена для хранения информации о голосованиях
    """
    title = models.CharField(max_length=255, verbose_name='Название')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата завершения')
    early_terminations = models.PositiveIntegerField(verbose_name='Максимальное кол-во голосов', null=True, blank=True)
    characters = models.ManyToManyField(
        to=Characters,
        related_name='characters_voting',
        verbose_name='Участники'
    )
    max_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Голосование: {self.title} | {self.early_terminations}'

    @property
    def is_active(self):
        ""
        now = timezone.now()
        return self.start_date < now <= self.end_date and self.max_votes < (self.early_terminations or float('inf'))

    @property
    def winner(self):
        """
        Получение победителя как персонажа с максимальным числом голосов для завершенных голосований
        """
        return self.characters.annotate(num_votes=models.Count('votes')).order_by('-num_votes').first() if not self.is_active else None

    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'


class Vote(models.Model):
    """Модель предназначена для хранения информации о голосах"""
    character = models.ForeignKey(Characters, on_delete=models.CASCADE, related_name='votes')
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE, related_name='votes')
    vote_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        creating = not self.pk  # Проверяем, создаем ли мы новое голосование
        super().save(*args, **kwargs)  # Вызвать исходный метод сохранения
        if not self.voting.is_active:
            raise ValueError('Голосование не активно')
        if creating:
            current_votes = Vote.objects.filter(character=self.character, voting=self.voting).count()
            voting = self.voting
            if voting.max_votes < current_votes:
                voting.max_votes = current_votes
                voting.save(update_fields=['max_votes'])
            if voting.early_terminations and current_votes >= voting.early_terminations:
                voting.end_date = timezone.now()
                voting.save(update_fields=['end_date'])

    class Meta:
        verbose_name = 'Голос'
        verbose_name_plural = 'Голоса'
