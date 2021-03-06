from django.conf import settings
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from ..comments.models import AbstractComment


class Post(models.Model):
    # Модель поста
    text = models.TextField('Текст', max_length=2000)
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    is_moderation = models.BooleanField('Модерация', default=True)
    view_count = models.PositiveIntegerField('Просмотры', default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'id {self.id}'

    def comments_count(self):
        return self.comments.count()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(AbstractComment, MPTTModel):
    # Модель комментария к посту
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return "{} - {}".format(self.user, self.post)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
