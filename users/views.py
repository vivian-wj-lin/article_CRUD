from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from django.contrib.auth.hashers import make_password, check_password

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


User = get_user_model()


class RegisterView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        username = request.data.get('username')

        hashed_password = make_password(password)

        user = authenticate(request, email=email, password=password)

        if User.objects.filter(email=email).exists():
            return Response({'message': 'Email已註冊'})

        user = User(email=email, username=username)
        user.password = hashed_password

        try:
            user.save()
        except:
            return Response({'message': '註冊失敗'})

        return Response({'message': '註冊成功'})


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        logger.debug(f"Email: {email}, Password: {password}")

        if user and user.is_active and check_password(password, user.password):
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(data)
        else:
            return Response({'message': 'Invalid credentials'}, status=400)
