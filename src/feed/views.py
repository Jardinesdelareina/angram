from rest_framework import permissions, viewsets, response
from .services import feed_service
from src.wall.serializers import ListPostSerializer, PostSerializer


class FeedView(viewsets.GenericViewSet):
    # Лента новостей
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListPostSerializer

    def list_feed(self, request, *args, **kwargs):
        queryset = feed_service.get_post_list(request.user)
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)

    def retrieve_feed(self, request, *args, **kwargs):
        instance = feed_service.get_single_post(kwargs.get('pk'))
        serializer = PostSerializer(instance)
        return response.Response(serializer.data)
