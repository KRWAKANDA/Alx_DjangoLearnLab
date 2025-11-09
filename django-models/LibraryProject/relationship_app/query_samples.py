from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    books = Book.objects.get(name=author_name)
    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")


def list_books_in_library(library_name):
    """List all books in a library."""
    try:
        library = Library.objects.get(name=library_name)
        print(f"Books in {library.name}:")
        for book in library.books.all():
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print("Library not found.")


def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print("Library not found.")
    except Librarian.DoesNotExist:
        print("No librarian assigned to this library.")


if __name__ == "__main__":
    query_books_by_author("George Orwell")
    list_books_in_library("Central Library")
    retrieve_librarian_for_library("Central Library")
