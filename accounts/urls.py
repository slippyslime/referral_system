from django.urls import path
from .views import SendAuthCodeView, VerifyAuthCodeView, UserProfileView

urlpatterns = [
    path('send-auth-code/', SendAuthCodeView.as_view(), name='send-auth-code'),
    path('verify-auth-code/', VerifyAuthCodeView.as_view(), name='verify-auth-code'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
]
