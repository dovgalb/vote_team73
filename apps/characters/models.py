from django.db import models


class Characters(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    photo = models.ImageField(verbose_name='Фото', blank=True, upload_to='images/%Y/%m/%d/')
    age = models.IntegerField(verbose_name='Возраст')
    short_bio = models.CharField(max_length=500, verbose_name='Биография')

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'

    def __str__(self):
        return f'Персонаж: {self.name}'
