from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework



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

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enable filter, search, ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching fields
    search_fields = ['title', 'author']

    # Ordering fields (you can expose all)
    ordering_fields = ['title', 'publication_year', 'id']

    # Optional: default ordering
    ordering = ['title']



