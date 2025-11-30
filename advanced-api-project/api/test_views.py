from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book


class BookAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="password123")
        self.client = APIClient()

        self.book = Book.objects.create(
            title="Test Book", author="John Doe", description="Sample Description", price=100
        )

        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book.id])

    # =====================
    # LIST VIEW TESTS
    # =====================
    def test_get_books_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("title", response.data[0])

    # =====================
    # CREATE TESTS
    # =====================
    def test_create_book_authenticated(self):
        self.client.login(username="tester", password="password123")
        data = {
            "title": "New Book",
            "author": "Alice",
            "description": "Description here",
            "price": 150,
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "New Book",
            "author": "Alice",
            "description": "Description here",
            "price": 150,
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # =====================
    # UPDATE TESTS
    # =====================
    def test_update_book_authenticated(self):
        self.client.login(username="tester", password="password123")
        data = {"title": "Updated Title"}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_update_book_unauthenticated(self):
        data = {"title": "Updated Title"}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # =====================
    # DELETE TESTS
    # =====================
    def test_delete_book_authenticated(self):
        self.client.login(username="tester", password="password123")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # =====================
    # SEARCH & FILTER TESTS
    # =====================
    def test_search_books(self):
        response = self.client.get(self.list_url + '?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_filter_books(self):
        response = self.client.get(self.list_url + '?author=John Doe')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_books(self):
        response = self.client.get(self.list_url + '?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
