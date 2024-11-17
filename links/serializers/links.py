from rest_framework import serializers
from links.models.links import Link
from django.contrib.auth import get_user_model


User = get_user_model()

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = (
            'pk', 'title', 'description', 'url', 'preview', 'type',
            'created_at', 'updated_at', 'collection', 'owner',
        )
        read_only_fields = ('owner', 'created_at', 'updated_at',)

    def _unique_url_validator(self, value, serializer):
        user = serializer.context['request'].user
        if Link.objects.filter(url=value, owner=user).exists():
            raise serializers.ValidationError("У вас уже есть ссылка с этим URL.")
        else:
            return value

    def validate_url(self, value):
        return self._unique_url_validator(value, self)
