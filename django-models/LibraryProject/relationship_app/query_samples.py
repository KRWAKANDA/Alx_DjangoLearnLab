import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


author_name = "Jane Austen"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print("-", book.title)
except Author.DoesNotExist:
    print("Author not found.")


library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print("Library not found.")
except Librarian.DoesNotExist:
    print("No librarian assigned for this library.")


try:
    librarian = library.librarian  
    print(f"\nLibrarian for {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print("No librarian assigned for this library.")


