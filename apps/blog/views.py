from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Post, PostCategory
from .forms import CommentForm, BlogForm, EditBlogForm
from django.shortcuts import render, get_object_or_404


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blogs/show_blogs.html"
    paginate_by = 3
    cats = PostCategory.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_menu = PostCategory.objects.all()
        context = super().get_context_data(object_list=None, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddBlogView(CreateView):
    model = Post
    form_class = BlogForm
    template_name = "blogs/add_post.html"
    success_url = reverse_lazy("blogs:show_all")


class UpdateBlogView(UpdateView):
    model = Post
    template_name = "blogs/update_post.html"
    # fields = ["title", "slug", "blog_category", "content"]
    form_class = EditBlogForm
    success_url = reverse_lazy("blogs:show_all")


class DeleteBlogView(DeleteView):
    model = Post
    template_name = "blogs/delete_post.html"
    success_url = reverse_lazy("blogs:show_all")


def post_detail(request, slug):
    model = Post
    template_name = "blogs/post_detail.html"
    post = get_object_or_404(model, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {"post": post, "comments": comments, "new_comment": new_comment, "comment_form": comment_form},
    )
