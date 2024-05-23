from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    # model = CustomUser
    # list_display = ['email', 'username',]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"), 
            {
                "fields": (
                    "last_name", 
                    "first_name", 
                    "patronymic", 
                    "email",
                    "avatar",
                )
            }
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ['username', 'email', 'get_full_name']

admin.site.register(CustomUser, CustomUserAdmin)