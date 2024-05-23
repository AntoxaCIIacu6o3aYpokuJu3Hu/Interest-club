from django.db import models
from django.contrib.auth.models import AbstractUser


def user_avatar_path(instance, filename):
    return f"static/avatars/user_{instance.id}/{filename}"


class CustomUser(AbstractUser):
    patronymic = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True)

    def get_avatar_path(self):
        return f'static/avatars/{self.id}.'

    def __str__(self):
        return self.username
    
    def get_full_name(self):
        full_name = f'{self.last_name} {self.first_name}'
        if self.patronymic:
            full_name += f' {self.patronymic}'
        return full_name