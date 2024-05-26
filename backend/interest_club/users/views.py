from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from users.models import CustomUser
from users.serializers import RegistrationSerializer, ProfileSerializer, UserSummarySerializer
from users.permissions import IsThatUser


class Registration(APIView):
    serializer_class = RegistrationSerializer

    @extend_schema(summary="Register new user", auth=[])
    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh_token = RefreshToken.for_user(user)
            return Response(
                {
                    'refresh': str(refresh_token),
                    'access': str(refresh_token.access_token),
                }, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Profile(APIView):
    permission_classes = [IsThatUser]
    serializer_class = ProfileSerializer

    @extend_schema(summary="Get user profile")
    def get(self, request, format=None):
        user = request.user
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    @extend_schema(summary="Update existing user")
    def put(self, request, format=None):
        user = request.user
        serializer = ProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserSummary(APIView):
    serializer_class = UserSummarySerializer

    @extend_schema(summary="Get user summary (fullname + avatar) by id")
    def get(self, request, pk, format=None):
        user = get_object_or_404(CustomUser, pk=pk)
        serializer = UserSummarySerializer(user)
        return Response(serializer.data)