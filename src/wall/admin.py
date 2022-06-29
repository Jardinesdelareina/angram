from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from src.wall.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Посты
    list_display = ('user', 'is_published', 'create_date', 'is_moderation', 'view_count', 'id')


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    # Комментарии к постам
    list_display = ('user', 'post', 'created_date', 'update_date', 'is_published', 'id')
    mptt_level_indent = 15
