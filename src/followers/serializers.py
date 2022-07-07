from rest_framework import serializers
from ..profiles.serializers import GetUserByForowersSerializer
from .models import Follower


class GetListFollowersSerializers(serializers.ModelSerializer):
    # Вывод списка подписчиков
    subscriber = GetUserByForowersSerializer(many=True, read_only=True)
    class Meta:
        model = Follower
        fields = ('subscriber',)
