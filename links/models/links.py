from django.db import models

from config import settings
from link_collections.models.collection import Collection
from links.services import get_page_data
from users.models.users import NULLABLE


class Link(models.Model):
    TYPE_CHOICES = [
        ('website', 'Website'),
        ('book', 'Book'),
        ('article', 'Article'),
        ('music', 'Music'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255, verbose_name='заголовок страницы', **NULLABLE)
    description = models.TextField(verbose_name='краткое описание', **NULLABLE)
    url = models.URLField(verbose_name='ссылка на страницу')
    preview = models.ImageField(upload_to='link_previews/', verbose_name='превью ссылки', **NULLABLE)
    type = models.CharField(default='website', max_length=20, choices=TYPE_CHOICES, verbose_name='тип ссылки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата и время обновления')

    collection = models.ManyToManyField(Collection, related_name='links', verbose_name='коллекция', blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_links',
                              verbose_name='владелец ссылки')

    def save(self, *args, **kwargs):
        if not self.pk:
            page_data = get_page_data(self.url)
            if page_data:
                self.title = page_data.get('title', '')
                self.description = page_data.get('description', '')
                self.type = page_data.get('type', 'website')
                image = page_data.get('image')
                if image:
                    self.preview.save(f'preview_{self.title[:15]}.jpg', image, save=False)

        super(Link, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.url} - {self.owner}'

    class Meta:
        verbose_name = 'ссылка'
        verbose_name_plural = 'ссылки'