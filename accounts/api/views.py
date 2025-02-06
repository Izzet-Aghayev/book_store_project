from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate, login, logout

from ..models import (
    User,
    Profile
)

from .serializers import (
    RegisetrSerializer,
    LoginSerializer,
    ProfileSerializer
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
    "email": "user1@gmail.com",
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

                if user is not None:
                    login(request, user)

                    return Response({'detail': 'Hesaba daxil oldunuz'}, status=status.HTTP_200_OK)
                
                return Response({'detail': 'Email və ya şifrə yanlışdır'}, status=status.HTTP_401_UNAUTHORIZED)
            
            return Response(serializer.errore, status=status.HTTP_400_BAD_REQUEST)
        


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'detail': 'Hesabdan çıxıldı'}, status=status.HTTP_401_UNAUTHORIZED)



class DeleteUserAPIView(APIView):
    def post(self, request):
        user = request.user
        if user.is_employee == 0:
            user.is_active = False

            user.save()

            return Response({'detail': 'Hesab silindi'}, status=status.HTTP_202_ACCEPTED)
        
        return Response({'detail': 'Admin hesabı silinə bilməz'}, status=status.HTTP_403_FORBIDDEN)



class ProfileUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        if user.is_employee==0:
            profile = Profile.objects.get(user=user)
            serializer = ProfileSerializer(profile, data = request.data, partial=True)

            if serializer.is_valid():
                serializer.save()

                return Response({'detail': 'Profil yeniləndi'}, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({'detail': 'İnzibatçı profili dəyişilə bilməz'}, status=status.HTTP_400_BAD_REQUEST)

'''

{
    "account_balance": 168,
    "profile_image": null
}

'''