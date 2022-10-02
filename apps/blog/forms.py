from .models import Comment, Post, PostCategory
from django import forms

# name cals two times in values_list() to get correct feedback from database
CATEGORY_CHOICES = PostCategory.objects.all().values_list("name", "name")
CATEGORY_CHOICES_LIST = []

for category in CATEGORY_CHOICES:
    CATEGORY_CHOICES_LIST.append(category)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "slug", "author", "blog_category", "content")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "blog_category": forms.Select(choices=CATEGORY_CHOICES_LIST, attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }


class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "slug", "blog_category", "content")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "blog_category": forms.Select(choices=CATEGORY_CHOICES_LIST, attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body")
