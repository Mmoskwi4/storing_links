from rest_framework import serializers

from links.models.links import Link



class LinkSerializer(serializers.ModelSerializer):

    def validate_url(self, value):
        user = serializer.context['request'].user
        if Link.objects.filter(url=value, owner=user).exists():
            raise serializers.ValidationError("У вас уже есть ссылка с этим URL.")
        else:
            return value

    class Meta:
        model = Link
        fields = (
            'pk', 'title', 'description', 'url', 'preview', 'type',
            'created_at', 'updated_at', 'collection', 'owner',
        )
        read_only_fields = ('owner', 'created_at', 'updated_at',)