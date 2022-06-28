from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import CustomUser
from .serializers import *

class CustomUserView(ModelViewSet):
    # Вывод профиля пользователя
    serializer_class = GetCustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)


class CustomUserPublicView(ModelViewSet):
    # Вывод публичного профиля пользователя
    queryset = CustomUser.objects.all()
    serializer_class = GetCustomUserPublicSerializer
    permission_classes = [permissions.AllowAny]
