from src.wall.models import Post


def feed(user):
    # Вывод постов всех подписчиков пользователя с сортировкой по дате создания (лента новостей)
    posts = Post.objects.filter(user__owner__subscriber_id=1).order_by('-create_date')\
        .select_related('user').prefetch_related('comments')
