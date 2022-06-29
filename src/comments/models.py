from django.db import models


class AbstractComment(models.Model):
    # Абстрактная модель комментария
    text = models.TextField('Комментарий', max_length=500)
    created_date = models.DateTimeField('Дата комментария', auto_now_add=True)
    update_date = models.DateTimeField('Дата изменения комментария', auto_now=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    is_deleted = models.BooleanField('Удалено', default=False)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        abstract = True
