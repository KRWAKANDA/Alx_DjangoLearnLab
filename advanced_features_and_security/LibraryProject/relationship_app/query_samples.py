import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "Jane Austen"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print("-", book.title)
except Author.DoesNotExist:
    print("Author not found.")

# 2. List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print("-", book.title)
except Library.DoesNotExist:
    print("Library not found.")

# 3. Retrieve the librarian for a library
try:
    librarian = library.librarian  # thanks to related_name='librarian'
    print(f"\nLibrarian for {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print("No librarian assigned for this library.")
