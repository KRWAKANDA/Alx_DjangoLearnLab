from rest_framework import generics, permissions
from .models import Book
from .serialializer import BookSerializer


# ============================
#   BOOK LIST VIEW
# ============================
class BookListView(generics.ListAPIView):
    """
    Retrieves all Book instances.
    Read-only: No authentication required.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access


# ============================
#   BOOK DETAIL VIEW
# ============================
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single Book by ID.
    Read-only for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ============================
#   BOOK CREATE VIEW
# ============================
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new Book instance.
    Restricted to authenticated users.
    Includes custom validation and metadata processing.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom hook allowing additional processing before save.
        """
        # You could add extra metadata or logic here
        serializer.save()


# ============================
#   BOOK UPDATE VIEW
# ============================
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing Book instance.
    Only authenticated users can update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom pre-save hook for update operations.
        """
        serializer.save()


# ============================
#   BOOK DELETE VIEW
# ============================
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes an existing Book instance.
    Only authenticated users can delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
