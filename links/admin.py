from django.contrib import admin

from links.models.links import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'description', 'url', 'preview',
        'type', 'created_at', 'updated_at', 'owner',
    )
    readonly_fields = (
        'created_at',
        'created_by',
        'updated_at',
        'updated_by',
    )