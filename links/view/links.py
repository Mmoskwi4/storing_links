from drf_spectacular.utils import extend_schema_view, extend_schema
from links.models.links import Link
from links.permissions import IsOwner
from links.serializers.links import LinkSerializer
from users.permissions import IsSuperUser

from rest_framework import mixins
from common.views.mixins import ExtendetGenericView
from common.pagination import BasePagination

@extend_schema_view(
create=extend_schema(
        summary='Создание Ссылки', tags=['Передаваемые ссылки для хранения']),
)
class LinkCreateAPIView(ExtendetGenericView, mixins.CreateModelMixin):
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

@extend_schema_view(
list=extend_schema(
        summary='Ссылки', tags=['Передаваемые ссылки для хранения']),
)
class LinkListAPIView(ExtendetGenericView, mixins.ListModelMixin):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    pagination_class = BasePagination
    permission_classes = [IsOwner | IsSuperUser]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Link.objects.all()
        return Link.objects.filter(owner=self.request.user)

@extend_schema_view(
retrieve=extend_schema(
        summary='Ссылка', tags=['Передаваемые ссылки для хранения']),
)
class LinkRetrieveAPIView(ExtendetGenericView, mixins.RetrieveModelMixin):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsOwner | IsSuperUser]

@extend_schema_view(
    update=extend_schema(
        summary='Изменение Ссылки', tags=['Передаваемые ссылки для хранения']),
    partial_update=extend_schema(
        summary='Изменение частично Ссылки', tags=['Передаваемые ссылки для хранения']),
)
class LinkUpdateAPIView(ExtendetGenericView, mixins.UpdateModelMixin):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsOwner | IsSuperUser]

@extend_schema_view(
destroy=extend_schema(
        summary='Удаление Ссылки', tags=['Передаваемые ссылки для хранения']),
)
class LinkDestroyAPIView(ExtendetGenericView, mixins.DestroyModelMixin):
    queryset = Link.objects.all()
    permission_classes = [IsOwner | IsSuperUser]