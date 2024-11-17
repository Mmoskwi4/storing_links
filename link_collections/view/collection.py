from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_view, extend_schema
from link_collections.models.collection import Collection
from link_collections.serializers.collection import CollectionSerializer
from links.permissions import IsOwner
from users.permissions import IsSuperUser

from common.pagination import BasePagination
from rest_framework import mixins
from common.views.mixins import ExtendetGenericView

User = get_user_model()

@extend_schema_view(
create=extend_schema(
        summary='Создание коллекции', tags=['Коллекции пользователей']),
)
class CollectionCreateAPIView(ExtendetGenericView, mixins.CreateModelMixin):
    serializer_class = CollectionSerializer


@extend_schema_view(
list=extend_schema(
        summary='Все коллекции', tags=['Коллекции пользователей']),
)
class CollectionListAPIView(ExtendetGenericView, mixins.ListModelMixin):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    pagination_class = BasePagination
    permission_classes = [IsOwner | IsSuperUser]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Collection.objects.all()
        return Collection.objects.filter(owner=self.request.user)

@extend_schema_view(
retrieve=extend_schema(
        summary='Коллекция', tags=['Коллекции пользователей']),
)
class CollectionRetrieveAPIView(ExtendetGenericView, mixins.RetrieveModelMixin):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    permission_classes = [IsOwner | IsSuperUser]

@extend_schema_view(
    update=extend_schema(
        summary='Изменение коллекции', tags=['Коллекции пользователей']),
    partial_update=extend_schema(
        summary='Изменение частично коллекцию', tags=['Коллекции пользователей']),
)
class CollectionUpdateAPIView(ExtendetGenericView, mixins.UpdateModelMixin):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    permission_classes = [IsOwner | IsSuperUser]

@extend_schema_view(
destroy=extend_schema(
        summary='Удаление коллекции', tags=['Коллекции пользователей']),
)
class CollectionDestroyAPIView(ExtendetGenericView, mixins.DestroyModelMixin):
    queryset = Collection.objects.all()
    permission_classes = [IsOwner | IsSuperUser]