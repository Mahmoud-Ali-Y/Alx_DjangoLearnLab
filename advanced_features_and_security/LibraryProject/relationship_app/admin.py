from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import CustomUser, UserProfile

class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = "CustomUser"
class UserAdmin(BaseUserAdmin):
    inlines = [CustomUserInline]

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)