from django.contrib import admin
from .models import *


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     # list_display = ['id', 'email']
#     pass


@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'user_id', 'slug']



