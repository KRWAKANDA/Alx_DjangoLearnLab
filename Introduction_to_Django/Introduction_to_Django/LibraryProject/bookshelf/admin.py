from django.contrib import admin
from .models import Book

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns displayed in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters on the right-hand side
    list_filter = ('publication_year', 'author')

    # Enable search by title and author
    search_fields = ('title', 'author')

