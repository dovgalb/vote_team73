from django.db import models
from datetime import time

from apps.characters.models import Characters


class Voting(models.Model):
    """
    Модель предназначена для хранения информации о голосованиях
    """
    title = models.CharField(max_length=255, verbose_name='Название')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата завершения')
    max_votes = models.IntegerField(verbose_name='Максимальное кол-во голосов')
    characters = models.ManyToManyField(
        to=Characters,
        related_name='characters_voting',
        verbose_name='Участники'
    )

    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'

    def __str__(self):
        return f'Голосование: {self.title} | {self.max_votes}'





