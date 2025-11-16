from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import BookForm, SearchForm


@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.all()
    if form.is_valid():
        q = form.cleaned_data.get("q")
        if q:
            # Safe ORM filtering (no raw SQL / no string concatenation)
            books = books.filter(title__icontains=q)  # parameterized by ORM
    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})


@permission_required("bookshelf.can_create", raise_exception=True)
@require_http_methods(["GET", "POST"])
def create_book(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.created_by = request.user
        book.save()
        return redirect("bookshelf:book_list")
    return render(request, "bookshelf/form_example.html", {"form": form, "title": "Create Book"})


@permission_required("bookshelf.can_edit", raise_exception=True)
@require_http_methods(["GET", "POST"])
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("bookshelf:book_list")
    return render(request, "bookshelf/form_example.html", {"form": form, "title": "Edit Book"})


@permission_required("bookshelf.can_delete", raise_exception=True)
@require_http_methods(["POST"])
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("bookshelf:book_list")
