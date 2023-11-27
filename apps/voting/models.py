from django.db import models
from django.db.models import Count, F, Max
from django.utils import timezone


class Voting(models.Model):
    """
    Модель предназначена для хранения информации о голосованиях
    """
    title = models.CharField(max_length=255, verbose_name='Название')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата завершения')
    early_terminations = models.PositiveIntegerField(verbose_name='Максимальное кол-во голосов', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    characters = models.ManyToManyField(
        to="Character",
        verbose_name='Участники',
        through='VotingCharacter',
    )

    def __str__(self):
        return f'Голосование: {self.title} | {self.early_terminations}'

    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'


class Character(models.Model):
    """
    Модель предназначена для хранения информации о персонажах.
    """
    name = models.CharField(max_length=255, verbose_name='ФИО')
    photo = models.ImageField(verbose_name='Фото', blank=True, upload_to='images/%Y/%m/%d/')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    short_bio = models.TextField(verbose_name='Биография')

    def __str__(self):
        return f'{self.id}. Персонаж: {self.name}'

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'


class VotingCharacter(models.Model):
    character = models.ForeignKey(to=Character, on_delete=models.CASCADE)
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)
    num_of_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'id:{self.id}. Голосование: {self.voting.title}, Участник: {self.character.name}'

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
