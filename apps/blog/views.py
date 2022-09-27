from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blogs/show_blogs.html"


class PostDetail(generic.DetailView):
    model = Post
    template_name = "blogs/post_detail.html"
