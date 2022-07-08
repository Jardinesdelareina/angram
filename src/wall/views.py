from rest_framework import permissions, generics
from ..base.classes import CreateUpdateDestroy, CreateRetrieveUpdateDestroy
from ..base.permissions import IsAuthor
from .models import Post, Comment
from .serializers import PostSerializer, ListPostSerializer, CreateCommentSerializer


class PostListView(generics.ListAPIView):
    # Список постов на стене пользователя
    serializer_class = ListPostSerializer

    def get_queryset(self):
        return Post.objects.filter(user_id=self.kwargs.get('pk'))\
            .select_related('user').prefetch_related('comments')


class PostView(CreateRetrieveUpdateDestroy):
    # CRUD поста
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().select_related('user').prefetch_related('comments')
    serializer_class = PostSerializer
    permission_classes_by_action = {
        'get_post': [permissions.AllowAny],
        'update_post': [IsAuthor],
        'destroy_post': [IsAuthor]
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentView(CreateUpdateDestroy):
    # CRUD комментариев к посту
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes_by_action = {
        'update_comment': [IsAuthor],
        'destroy_comment': [IsAuthor]
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
