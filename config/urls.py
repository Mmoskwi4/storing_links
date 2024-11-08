from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('links/', include('links.urls', namespace='links')),
    path('collections/', include('link_collections.urls', namespace='collections')),
]
