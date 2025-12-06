# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from django import forms
from .models import Post
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={'class': 'form-control', 'placeholder': 'Add tags separated by commas'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']
        

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}),
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']        


