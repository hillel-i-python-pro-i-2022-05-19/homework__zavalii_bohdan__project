from django.shortcuts import render

from apps.blog.models import Post


def category_view(request, cats):
    category_posts = Post.objects.filter(blog_category=cats)
    return render(request, "blogs/categories.html", {"cats": cats.title(), "category_posts": category_posts})
