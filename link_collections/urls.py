from django.urls import path, include
from link_collections.view import collection
from link_collections.apps import LinkCollectionsConfig
from rest_framework.routers import DefaultRouter


app_name = LinkCollectionsConfig.name

router = DefaultRouter()

router.register(r'create-collection', collection.CollectionCreateAPIView, 'create-collection')
router.register(r'list-collections', collection.CollectionListAPIView, 'list-collections')
router.register(r'retrieve-collection', collection.CollectionRetrieveAPIView, 'retrieve-collection')
router.register(r'update-collection', collection.CollectionUpdateAPIView, 'update-collection')
router.register(r'delete-collection', collection.CollectionDestroyAPIView, 'delete-collection')


urlpatterns = [

]

urlpatterns += path('collections/', include(router.urls)),