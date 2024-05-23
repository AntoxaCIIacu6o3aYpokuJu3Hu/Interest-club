from django.contrib import admin

from .models import SocialGroup, GroupRecord, Comment

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

admin.site.register(SocialGroup)
admin.site.register(GroupRecord, GroupRecordAdmin)