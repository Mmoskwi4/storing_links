# Generated by Django 5.1.2 on 2024-11-08 17:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('link_collections', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='заголовок страницы')),
                ('description', models.TextField(blank=True, null=True, verbose_name='краткое описание')),
                ('url', models.URLField(verbose_name='ссылка на страницу')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='link_previews/', verbose_name='превью ссылки')),
                ('type', models.CharField(choices=[('website', 'Website'), ('book', 'Book'), ('article', 'Article'), ('music', 'Music'), ('video', 'Video')], default='website', max_length=20, verbose_name='тип ссылки')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата и время обновления')),
                ('collection', models.ManyToManyField(blank=True, related_name='links', to='link_collections.collection', verbose_name='коллекция')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_links', to=settings.AUTH_USER_MODEL, verbose_name='владелец ссылки')),
            ],
            options={
                'verbose_name': 'ссылка',
                'verbose_name_plural': 'ссылки',
            },
        ),
    ]
