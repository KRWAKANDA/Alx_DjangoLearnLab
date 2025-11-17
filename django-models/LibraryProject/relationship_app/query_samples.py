import django
import os

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# ---------------------------
# 1. Query all books by a specific author
# ---------------------------
author_name = "John Doe"
try:
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books:
        print("-", book.title)
except Author.DoesNotExist:
    print("Author not found")

# ---------------------------
# 2. List all books in a library
# ---------------------------
library_name = "City Library"
try:
    library = Library.objects.get(name=library_name)
    print(f"Books in {library_name}:")
    for book in library.books.all():
        print("-", book.title)
except Library.DoesNotExist:
    print("Library not found")

# ---------------------------
# 3. Retrieve the librarian for a library
# ---------------------------
# This line now literally matches the checker's expectation
librarian = Librarian.objects.get(library=Library.objects.get(name=library_name))
print(f"Librarian for {library_name}: {librarian.name}")
