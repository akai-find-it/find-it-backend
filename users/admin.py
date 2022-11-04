from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering = ("email",)
    list_display = ("email",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_staff", "is_superuser", "user_permissions", "groups"),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password1",
                    "password2",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_staff", "is_superuser", "user_permissions", "groups"),
            },
        ),
    )


admin.site.register(get_user_model(), UserAdmin)
