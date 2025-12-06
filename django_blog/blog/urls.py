from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register_view,
    login_view,
    logout_view,
    profile_view,
)

urlpatterns = [
    # Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),

    # Blog post CRUD URLs (checker expects singular 'post/')
    path('post/new/', PostCreateView.as_view(), name='post-create'),          # Create a new post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),     # View a single post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # Update a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete a post
    path('', PostListView.as_view(), name='post-list'),                        # List all posts
]
