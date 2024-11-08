from django.db import models
from config import settings
from users.models.users import NULLABLE


class Collection(models.Model):
    name = models.CharField(max_length=150, verbose_name='название коллекции')
    description = models.TextField(verbose_name='краткое описание', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата и время обновления')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_collections',
                              verbose_name='владелец коллекции')

    def __str__(self):
        return f'{self.name} - {self.owner}'

    class Meta:
        verbose_name = 'коллекция'
        verbose_name_plural = 'коллекции'