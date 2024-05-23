from django.contrib import admin

from .models import SocialGroup, GroupRecord, Comment

admin.site.register(SocialGroup)
admin.site.register(GroupRecord)
admin.site.register(Comment)