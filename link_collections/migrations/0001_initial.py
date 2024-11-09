# Generated by Django 5.1.2 on 2024-11-08 17:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название коллекции')),
                ('description', models.TextField(blank=True, null=True, verbose_name='краткое описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата и время обновления')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_collections', to=settings.AUTH_USER_MODEL, verbose_name='владелец коллекции')),
            ],
            options={
                'verbose_name': 'коллекция',
                'verbose_name_plural': 'коллекции',
            },
        ),
    ]
