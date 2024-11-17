from django.urls import path, include
from api.spectacular.urls import urlpatterns as doc_urls
from users.urls import urlpatterns as user_urls
from link_collections.urls import urlpatterns as collections_urls
from links.urls import urlpatterns as links_urls

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_urls
urlpatterns += user_urls
urlpatterns += collections_urls
urlpatterns += links_urls