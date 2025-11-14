from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

User = get_user_model()


class CustomUserManager(BaseUserManager):
    """Manager for custom user model with email instead of username."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None  # disable username field
    email = models.EmailField(_("email address"), unique=True)

    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # email & password are required by default

    objects = CustomUserManager()

    def __str__(self):
        return self.email




class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"



