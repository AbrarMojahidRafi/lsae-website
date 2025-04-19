# blogs/forms.py
from django import forms
from .models import Blog, BlogImage

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

class BlogImageForm(forms.ModelForm):
    class Meta:
        model = BlogImage
        fields = ['image']
