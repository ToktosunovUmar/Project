from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from .serializer import UserCreateSerializer, UserAuthSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import ConfirmCode
import random
import string
from rest_framework.views import APIView


class AuthAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = User.objects.create_user(username=username, password=password,
                                        is_active=False)

        confirmation_password = ''.join(random.choices(string.digits, k=6))
        ConfirmCode.objects.create(user=user, password=confirmation_password)

        return Response(status=status.HTTP_201_CREATED,
                        data={'user_id': user.id, 'confirmation_password': confirmation_password})


class ConfirmAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        confirmation_password = request.data.get('confirmation_password')

        try:
            user = User.objects.get(username=username)
            user_confirm_password = ConfirmCode.objects.get(user=user)

            if user_confirm_password.password == confirmation_password:
                user.is_active = True
                user.save()
                user_confirm_password.delete()
                return Response({"message": "User confirmed activated."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid confirmation code."}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)
        if user:
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                return Response(data={'key': token.key})
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': 'User not confirmed'})
        return Response(status=status.HTTP_401_UNAUTHORIZED,
                        data={'error': 'User wrong'})
