
from django.urls import path
from .views import (
    RegistrationView,
    LoginView,
    LogoutView,
    UserDetailView,
    ChangePasswordView
)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('password/change/', ChangePasswordView.as_view(), name='password-change'),
]