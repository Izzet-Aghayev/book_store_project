from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout

from ..models import User
from .serializers import (
    RegisetrSerializer,
    LoginSerializer
)


class RegisterAPIView(APIView):
    def post(self, request):
        if request.method == 'POST':
            serializer = RegisetrSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                password = serializer.validated_data.get('password')

                User.objects.create_user(email=email, password=password)

                return Response({'detail': 'Qeydiyatdan keçdiniz'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''

{
    "email": "user5@gmail.com",
    "password": "Izzet-1409"
}

'''


class LoginAPIView(APIView):
    def post(self, request):
        if request.method == 'POST':
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                password = serializer.validated_data.get('password')

                user = authenticate(request, email=email, password=password)

                print(user)
                print(user.email)
                print(user.password)

                if user is not None:
                    login(request, user)

                    return Response({'detail': 'Hesaba daxil oldunuz'}, status=status.HTTP_200_OK)
                
                return Response({'detail': 'Email və ya şifrə yanlışdır'}, status=status.HTTP_401_UNAUTHORIZED)
            
            return Response(serializer.errore, status=status.HTTP_400_BAD_REQUEST)
        


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'detail': 'Hesabdan çıxıldı'}, status=status.HTTP_200_OK)
