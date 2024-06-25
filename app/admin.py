from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year', 'price', 'genre', 'created_at', 'updated_at')
    search_fields = ('title', 'author', 'genre')
