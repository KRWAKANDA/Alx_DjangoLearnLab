from django.urls import reverse
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
