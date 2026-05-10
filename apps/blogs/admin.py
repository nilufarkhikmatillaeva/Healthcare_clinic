from django.contrib import admin
from .models import Blog, Category, Tag, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_at']
    search_fields = ['title', 'author']
    list_filter = ['category', 'tags']
    filter_horizontal = ['tags']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'blog', 'created_at']
    search_fields = ['name', 'email']
