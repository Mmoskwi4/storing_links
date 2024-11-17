from django.contrib.auth import get_user_model
from rest_framework import serializers

from link_collections.models.collection import Collection
from links.models.links import Link
from common.serializers.mixins import ExtendedModelSerializer

User = get_user_model()

class CollectionSerializer(ExtendedModelSerializer):

    links_count = serializers.IntegerField(
        source="links.all.count", required=False, read_only=True
    )
    links = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Link.objects.all(), required=False
    )

    class Meta:
            model = Collection
            fields = (
                "pk",
                "name",
                "description",
                "links_count",
                "links",
                "created_at",
                "updated_at",
                "owner",
            )

    def _validate_links_owner(self, links, owner):
        for link in links:
            if link.owner != owner:
                raise serializers.ValidationError("Вы не можете добавлять свои ссылки в чужие коллекции.")
    
    def validate(self, data):
        if 'links' in data:
            self._validate_links_owner(data['links'], self.context['request'].user)
        return data

    
