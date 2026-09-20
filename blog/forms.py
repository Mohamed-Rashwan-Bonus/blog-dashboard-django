from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content', 'image', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسمك'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'اكتب تعليقك...'}),
        }
