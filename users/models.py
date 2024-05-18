from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    username = None
    email = models.EmailField(
        verbose_name='почта',
        unique=True
    )

    def __str__(self):
        return getattr(self, self.USERNAME_FIELD)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
