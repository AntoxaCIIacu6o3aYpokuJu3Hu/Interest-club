from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser


class ShortUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'last_name', 'first_name', 'patronymic', 'avatar']
        read_only_fields = ['id']


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'last_name', 'first_name', 'patronymic', 'avatar', 'email', 'username', 'password']
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True},
            'last_name': {'required': True},
            'first_name': {'required': True},
            'email': {'required': True},
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'last_name', 'first_name', 'patronymic', 'avatar', 'email', 'username', 'password']
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'username': {'required': False},
        }
