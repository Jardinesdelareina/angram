from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserConfig(AbstractBaseUser):
    # Кастомная модель абстрактного юзера
    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)