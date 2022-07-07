from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Кастомная модель пользователя
    GENDER = (
        ('male', 'Мужской'),
        ('female', 'Женский')
    )
    middle_name = models.CharField('Отчество', max_length=80)
    first_login = models.DateTimeField('Первый вход', null=True)
    phone = models.CharField('Телефон', max_length=14)
    avatar = models.ImageField('Аватар', upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField('О себе', blank=True, null=True)
    github = models.CharField('GitHub', max_length=500, blank=True, null=True)
    birthday = models.DateField('Дата рождения', blank=True, null=True)
    gender = models.CharField('Пол', max_length=7, choices=GENDER, default='male')
    technology = models.ManyToManyField('Technology', related_name='users')


class Technology(models.Model):
    # Модель технологий
    title = models.CharField('Технологии', max_length=100)

    def __str__(self):
        return self.title
