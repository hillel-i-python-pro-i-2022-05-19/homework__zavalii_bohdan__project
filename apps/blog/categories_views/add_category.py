from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.blog.models import PostCategory


class AddCategoryView(CreateView):
    model = PostCategory
    fields = "__all__"
    template_name = "blogs/add_category.html"
    success_url = reverse_lazy("blogs:show_all")
