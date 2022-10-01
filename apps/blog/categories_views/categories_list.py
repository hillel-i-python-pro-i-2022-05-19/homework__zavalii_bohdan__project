from django.views import generic

from apps.blog.models import PostCategory


class CategoriesList(generic.ListView):
    model = PostCategory
    template_name = "blogs/show_blogs.html"
