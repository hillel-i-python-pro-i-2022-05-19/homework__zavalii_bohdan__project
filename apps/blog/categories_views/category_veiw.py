from django.shortcuts import render

from apps.blog.models import Post


def category_view(request, cats):
    category_posts = Post.objects.filter(blog_category=cats.replace("-", " "))
    return render(
        request, "blogs/categories.html", {"cats": cats.title().replace("-", " "), "category_posts": category_posts}
    )
