from django.urls import path

from links.view.links import LinkCreateAPIView, LinkListAPIView, LinkRetrieveAPIView, LinkUpdateAPIView, \
    LinkDestroyAPIView
from links.apps import LinksConfig

app_name = LinksConfig.name

urlpatterns = [
    path('create/', LinkCreateAPIView.as_view(), name='link-create'),
    path('links_list/', LinkListAPIView.as_view(), name='link-list'),
    path('detail/<int:pk>/', LinkRetrieveAPIView.as_view(), name='link-detail'),
    path('update/<int:pk>/', LinkUpdateAPIView.as_view(), name='link-update'),
    path('delete/<int:pk>/', LinkDestroyAPIView.as_view(), name='link-delete'),
]