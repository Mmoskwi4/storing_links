from django.contrib.auth import get_user_model
from django.db import models
from config import settings
from users.models.users import NULLABLE
from common.models.mixins import InfoMixin

User = get_user_model()


class Collection(InfoMixin):
    name = models.CharField(max_length=150, verbose_name='название коллекции')
    description = models.TextField(verbose_name='краткое описание', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_collections',
                              verbose_name='владелец коллекции')

    class Meta:
        verbose_name = 'коллекция'
        verbose_name_plural = 'коллекции'
        
    def __str__(self):
        return f'{self.name} - {self.owner}'
