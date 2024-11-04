from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Gallery(models.Model):
    name = models.CharField("Название", max_length=50)
    director = models.ForeignKey(
        User, models.RESTRICT, 'gallery_director',
        verbose_name='Директор'
    )


    class Meta:
        verbose_name = 'Геллерея'
        verbose_name_plural = 'Геллереи'
        ordering = ('name',)
