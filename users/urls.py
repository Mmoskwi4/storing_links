from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django_rest_passwordreset.urls import add_reset_password_urls_to_router

from users.views import users

router = DefaultRouter()

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/reg/', users.RegistrationView.as_view(), name='reg'),
    path('users/reg/change_password/', users.ChangePasswordView.as_view(), name='change_passwd'),
    path('users/reg/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

urlpatterns += path('users/', include(router.urls)),