from rest_framework import serializers

from link_collections.models.collection import Collection
from links.models.links import Link


class CollectionSerializer(serializers.ModelSerializer):

    links_count = serializers.IntegerField(source='links.all.count', required=False, read_only=True)
    links = serializers.PrimaryKeyRelatedField(many=True, queryset=Link.objects.all(), required=False)

    def validate(self, data):
        for link in links:
            if link.owner != owner:
                raise serializers.ValidationError("Вы не можете добавлять свои ссылки в чужие коллекции.")
            else:
                return data

    class Meta:
        model = Collection
        fields = (
            'pk', 'name', 'description', 'links_count', 'links',
            'created_at', 'updated_at', 'owner',
        )
        read_only_fields = ('owner', 'created_at', 'updated_at',)