from django.contrib import admin

from .models import SocialGroup, GroupRecord

admin.site.register(SocialGroup)
admin.site.register(GroupRecord)