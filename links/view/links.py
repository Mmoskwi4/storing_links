from rest_framework import generics

from links.models.links import Link
from links.paginators import LinkPaginator
from links.permissions import IsOwner
from links.serializers.links import LinkSerializer
from users.permissions import IsSuperUser


class LinkCreateAPIView(generics.CreateAPIView):
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LinkListAPIView(generics.ListAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    pagination_class = LinkPaginator
    permission_classes = [IsOwner | IsSuperUser]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Link.objects.all()
        return Link.objects.filter(owner=self.request.user)


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsOwner | IsSuperUser]


class LinkUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsOwner | IsSuperUser]


class LinkDestroyAPIView(generics.DestroyAPIView):
    queryset = Link.objects.all()
    permission_classes = [IsOwner | IsSuperUser]