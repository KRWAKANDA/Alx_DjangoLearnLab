# relationship_app/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']  # Fields to include in the form
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
