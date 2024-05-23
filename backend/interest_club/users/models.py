from django.db import models
from django.contrib.auth.models import AbstractUser


def user_avatar_path(instance, filename):
    return f"static/avatars/user_{instance.id}/{filename}"


class CustomUser(AbstractUser):
    patronymic = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(upload_to=user_avatar_path, null=True, blank=True)

    def __str__(self):
        return self.username
    
    def get_full_name(self):
        full_name = f'{self.last_name} {self.first_name}'
        if self.patronymic:
            full_name += f' {self.patronymic}'
        return full_name
    
    class Meta:
        ordering = ['last_name', 'first_name', 'patronymic']