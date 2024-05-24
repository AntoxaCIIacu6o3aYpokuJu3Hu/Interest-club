import uuid
from django.db import models
from users.models import CustomUser


def user_group_logo_path(instance, filename):
    return f"static/groups/group_{instance.id}/logo/{filename}"

class SocialGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='group_owner')
    users = models.ManyToManyField(CustomUser, related_name='users', blank=True)
    name = models.CharField(max_length=150)
    summary = models.CharField(max_length=300)
    description = models.TextField()
    logo = models.ImageField(upload_to=user_group_logo_path, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]


class GroupRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='record_owner')
    group = models.ForeignKey(SocialGroup, on_delete=models.CASCADE, related_name='record_parent')
    name = models.CharField(max_length=150)
    description = models.TextField()
    created_date = models.DateTimeField("created date")
    event_date = models.DateTimeField("event date", null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["created_date"]


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment_owner')
    parent = models.ForeignKey(GroupRecord, on_delete=models.CASCADE, related_name='comment_parent')
    text = models.TextField()
    created_date = models.DateTimeField("created date")

    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ["created_date"]