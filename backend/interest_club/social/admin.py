from django.contrib import admin

from .models import SocialGroup, GroupRecord, Comment


class GroupRecordInline(admin.StackedInline):
    model = GroupRecord
    extra = 0

class SocialGroupAdmin(admin.ModelAdmin):
    fieldsets = [
        ("User info", {"fields": ["owner", "users"]}),
        ("Content", {"fields": ["name", "summary", "description", "logo"]}),
    ]
    inlines = [GroupRecordInline]


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class GroupRecordAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["author", "name", "description"]}),
        ("Creation date", {"fields": ["created_date"], "classes": ["collapse"]}),
        ("Event date", {"fields": ["event_date"], "classes": ["collapse"]}),
    ]
    inlines = [CommentInline]

admin.site.register(SocialGroup, SocialGroupAdmin)
admin.site.register(GroupRecord, GroupRecordAdmin)