from django.contrib import admin

from link_collections.models.collection import Collection


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):

    list_display = (
        'pk', 'name', 'description', 'created_at',
        'updated_at', 'owner',
    )