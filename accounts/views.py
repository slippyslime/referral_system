from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.core.cache import cache
import random
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import UserProfileSerializer


class SendAuthCodeView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Генерация и сохранение кода
        auth_code = random.randint(1000, 9999)
        cache.set(phone_number, auth_code, timeout=300)  # Сохранение на 5 минут

        print(f"Auth code for {phone_number}: {auth_code}")

        # Имитируем задержку и отправку
        return Response({'message': 'Code sent successfully'}, status=status.HTTP_200_OK)


class VerifyAuthCodeView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        auth_code = request.data.get('auth_code')

        if not phone_number or not auth_code:
            return Response({'error': 'Phone number and auth code are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Проверка кода
        cached_code = cache.get(phone_number)
        if cached_code is None or str(cached_code) != str(auth_code):
            return Response({'error': 'Invalid code'}, status=status.HTTP_400_BAD_REQUEST)

        # Создание пользователя, если его нет
        user, created = User.objects.get_or_create(phone_number=phone_number)
        return Response({'message': 'Verification successful', 'invite_code': user.invite_code},
                        status=status.HTTP_200_OK)


class UserProfileView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
