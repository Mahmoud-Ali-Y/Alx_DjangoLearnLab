from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Book, CustomUser
class Book(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('author', 'publication_year')

class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = "CustomUser"
class CustomUserAdmin(BaseUserAdmin):
    inlines = [CustomUserInline]

# Register your models here.
admin.site.register(Book)
# admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)