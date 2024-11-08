from django.urls import path

from link_collections.view.collection import CollectionCreateAPIView, CollectionListAPIView, \
    CollectionRetrieveAPIView, CollectionUpdateAPIView, CollectionDestroyAPIView
from link_collections.apps import LinkCollectionsConfig

app_name = LinkCollectionsConfig.name

urlpatterns = [
    path('create/', CollectionCreateAPIView.as_view(), name='collection-create'),
    path('collection_list/', CollectionListAPIView.as_view(), name='collection-list'),
    path('detail/<int:pk>/', CollectionRetrieveAPIView.as_view(), name='collection-detail'),
    path('update/<int:pk>/', CollectionUpdateAPIView.as_view(), name='collection-update'),
    path('delete/<int:pk>/', CollectionDestroyAPIView.as_view(), name='collection-delete'),
]