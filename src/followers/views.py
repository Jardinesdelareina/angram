from rest_framework import generics, permissions, views, response

from ..profiles.models import CustomUser
from .models import Follower
from .serializers import GetListFollowersSerializers


class ListFollowersView(generics.ListAPIView):
    # Вывод списка подписчиков пользователя
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GetListFollowersSerializers

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class FollowerView(views.APIView):
    # Добавление/удаление подписчиков
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user = CustomUser.objects.get(id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        Follower.objects.create(subscriber=request.user, user=user)
        return response.Response(status=204)

    def delete(self, request, pk):
        try:
            follower = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        follower.delete()
        return response.Response(status=204)
