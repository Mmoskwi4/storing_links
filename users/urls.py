from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import users


urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/reg/', users.RegistrationView.as_view(), name='reg'),
    path('users/change-password/', users.ChangePasswordView.as_view(), name='change_password'),
    path('users/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]