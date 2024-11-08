from rest_framework import generics
from drf_spectacular.utils import extend_schema_view, extend_schema
from links.models.links import Link
from links.paginators import LinkPaginator
from links.permissions import IsOwner
from links.serializers.links import LinkSerializer
from users.permissions import IsSuperUser

@extend_schema_view(
post=extend_schema(
        summary='Создание Ссылки', tags=['Передаваемые ссылки для хранения']),
)
class LinkCreateAPIView(generics.CreateAPIView):
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

@extend_schema_view(
get=extend_schema(
        summary='Ссылки', tags=['Передаваемые ссылки для хранения']),
)
class LinkListAPIView(generics.ListAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    pagination_class = LinkPaginator
    permission_classes = [IsOwner | IsSuperUser]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Link.objects.all()
        return Link.objects.filter(owner=self.request.user)

@extend_schema_view(
get=extend_schema(
        summary='Ссылка', tags=['Передаваемые ссылки для хранения']),
)
class LinkRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsOwner | IsSuperUser]

@extend_schema_view(
    patch=extend_schema(
        summary='Изменение Ссылки', tags=['Передаваемые ссылки для хранения']),
    put=extend_schema(
        summary='Изменение частично Ссылки', tags=['Передаваемые ссылки для хранения']),
)
class LinkUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsOwner | IsSuperUser]

@extend_schema_view(
delete=extend_schema(
        summary='Удаление Ссылки', tags=['Передаваемые ссылки для хранения']),
)
class LinkDestroyAPIView(generics.DestroyAPIView):
    queryset = Link.objects.all()
    permission_classes = [IsOwner | IsSuperUser]