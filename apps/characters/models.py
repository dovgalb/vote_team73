from django.db import models


class Characters(models.Model):
    """
    Модель предназначена для хранения информации о персонажах.
    """
    name = models.CharField(max_length=255, verbose_name='ФИО')
    photo = models.ImageField(verbose_name='Фото', blank=True, upload_to='images/%Y/%m/%d/')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    short_bio = models.TextField(verbose_name='Биография')

    def __str__(self):
        return f'{self.id}. Персонаж: {self.name}'

    def is_in_voting(self, voting):
        if self.characters_voting.filter(pk=voting.pk).exists():
            return True
        raise Characters.DoesNotExist

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'

