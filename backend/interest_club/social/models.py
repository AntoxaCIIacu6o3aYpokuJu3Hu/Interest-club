import uuid
from django.db import models
from users.models import CustomUser


def user_group_logo_path(instance, filename):
    return f"static/groups/group_{instance.id}/logo/{filename}"

class SocialGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')
    users = models.ManyToManyField(CustomUser, related_name='users', blank=True)
    name = models.CharField(max_length=150)
    summary = models.CharField(max_length=300)
    description = models.TextField()
    logo = models.ImageField(upload_to=user_group_logo_path, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]