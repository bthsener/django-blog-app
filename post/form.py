from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['timestamp']
        fields = [
            'name',
            'content',
        ]

    def __init__(self, *args, **kwargs):
        print("Hello")
        super().__init__(*args, **kwargs)