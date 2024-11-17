from django.urls import path, include
from links.view import links
from links.apps import LinksConfig
from rest_framework.routers import DefaultRouter

app_name = LinksConfig.name

router = DefaultRouter()

router.register(r'create-collection', links.LinkCreateAPIView, 'create-link')
router.register(r'list-collections', links.LinkListAPIView, 'list-links')
router.register(r'retrieve-collection', links.LinkRetrieveAPIView, 'retrieve-link')
router.register(r'update-collection', links.LinkUpdateAPIView, 'update-link')
router.register(r'delete-collection', links.LinkDestroyAPIView, 'delete-link')

urlpatterns = [

]

urlpatterns += path('links/', include(router.urls)),