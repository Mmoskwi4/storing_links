from rest_framework import generics
from drf_spectacular.utils import extend_schema_view, extend_schema
from link_collections.models.collection import Collection
from link_collections.paginators import CollectionPaginator
from link_collections.serializers.collection import CollectionSerializer
from links.permissions import IsOwner
from users.permissions import IsSuperUser


@extend_schema_view(
post=extend_schema(
        summary='Создание коллекции', tags=['Коллекции пользователей']),
)
class CollectionCreateAPIView(generics.CreateAPIView):

    serializer_class = CollectionSerializer

    def post(self, serializer):

        serializer.save(owner=self.request.user)

@extend_schema_view(
get=extend_schema(
        summary='Все коллекции', tags=['Коллекции пользователей']),
)
class CollectionListAPIView(generics.ListAPIView):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    pagination_class = CollectionPaginator
    permission_classes = [IsOwner | IsSuperUser]

    def get_queryset(self):

        if self.request.user.is_superuser:
            return Collection.objects.all()
        return Collection.objects.filter(owner=self.request.user)

@extend_schema_view(
get=extend_schema(
        summary='Коллекция', tags=['Коллекции пользователей']),
)
class CollectionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    permission_classes = [IsOwner | IsSuperUser]

@extend_schema_view(
    patch=extend_schema(
        summary='Изменение коллекции', tags=['Коллекции пользователей']),
    put=extend_schema(
        summary='Изменение частично коллекцию', tags=['Коллекции пользователей']),
)
class CollectionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    permission_classes = [IsOwner | IsSuperUser]

@extend_schema_view(
delete=extend_schema(
        summary='Удаление коллекции', tags=['Коллекции пользователей']),
)
class CollectionDestroyAPIView(generics.DestroyAPIView):
    queryset = Collection.objects.all()
    permission_classes = [IsOwner | IsSuperUser]