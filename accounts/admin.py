from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = (
        'email',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    list_filter = (
        'is_superuser',
        'is_active',
    )
    ordering = ('email',)
    filter_horizontal = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser',)}),
    )

admin.site.register(User, UserAdmin)