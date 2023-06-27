from django.contrib import admin


from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.apps import apps

admin.site.site_header = "Django SAAS"


class CustomUserAdmin(UserAdmin):
    # form = UserChangeForm
    # add_form = UserCreationForm

    list_display = ("email", "is_active", "is_superuser", "is_active")
    list_filter = ("is_superuser", "is_active")
    fieldsets = (
        ("Details", {"fields": ("email", "password")}),
        (
            "Access",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                    "groups",
                )
            },
        ),
    )
    add_fieldsets = (
        ("Details", {"fields": ("email", "password1", "password2")}),
        # ('Access', {'fields': ('is_active', 'is_staff',
        #  'is_superuser', 'user_permissions', 'groups')}),
    )
    search_fields = ("email",)
    ordering = ("email",)
    # filter_horizontal = ()

    # def client(self, obj):
    #     return obj.client
    # def schema(self, obj):
    #     return obj.client.schema_name
    # def is_active(self, obj):
    #     return obj.client.is_active

app = apps.get_app_config('authentication')
# app. = 'Authentication 2'
User = get_user_model()

admin.site.register(User, CustomUserAdmin)
