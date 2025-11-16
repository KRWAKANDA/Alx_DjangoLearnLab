from django import forms
from .models import Book
from django.core.validators import MaxLengthValidator


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "profile_photo"]

    # Example extra validation
    title = forms.CharField(max_length=255, validators=[MaxLengthValidator(255)])

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        # simple sanitization/transformation example
        return title


class SearchForm(forms.Form):
    q = forms.CharField(required=False, max_length=100)

    def clean_q(self):
        q = self.cleaned_data.get("q", "")
        # additional validation/sanitization if needed
        return q.strip()
