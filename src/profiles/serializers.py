from rest_framework import serializers
from .models import CustomUser


class GetCustomUserSerializer(serializers.ModelSerializer):
    # Вывод информации о пользователе
    avatar = serializers.ImageField(read_only=True)
    class Meta:
        model = CustomUser
        exclude = (
            'password',
            'last_login',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )


class GetCustomUserPublicSerializer(serializers.ModelSerializer):
    # Вывод публичной информации о пользователе
    class Meta:
        model = CustomUser
        exclude = (
            'email',
            'phone',
            'password',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )
