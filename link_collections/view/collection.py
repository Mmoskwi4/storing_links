from rest_framework import generics

from link_collections.models.collection import Collection
from link_collections.paginators import CollectionPaginator
from link_collections.serializers.collection import CollectionSerializer
from links.permissions import IsOwner
from users.permissions import IsSuperUser


class CollectionCreateAPIView(generics.CreateAPIView):

    serializer_class = CollectionSerializer

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)


class CollectionListAPIView(generics.ListAPIView):

    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    pagination_class = CollectionPaginator
    permission_classes = [IsOwner | IsSuperUser]

    def get_queryset(self):

        if self.request.user.is_superuser:
            return Collection.objects.all()
        return Collection.objects.filter(owner=self.request.user)


class CollectionRetrieveAPIView(generics.RetrieveAPIView):

    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    permission_classes = [IsOwner | IsSuperUser]


class CollectionUpdateAPIView(generics.UpdateAPIView):

    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    permission_classes = [IsOwner | IsSuperUser]


class CollectionDestroyAPIView(generics.DestroyAPIView):
    queryset = Collection.objects.all()
    permission_classes = [IsOwner | IsSuperUser]