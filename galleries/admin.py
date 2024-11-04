from django.contrib import admin
from galleries.models.model_gallery import Gallery


@admin.register(Gallery)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director',)