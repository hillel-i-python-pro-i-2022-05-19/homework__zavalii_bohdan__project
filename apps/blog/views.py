from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from .models import Post, PostCategory
from .forms import CommentForm, BlogForm, EditBlogForm
from django.shortcuts import render, get_object_or_404


def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    liked = False  # flake8: noqa: F841

    # If the user who clicked on 👍 already exists, then we remove him
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False  # flake8: noqa: F841
    else:
        # else we add/assign a like to the exact user
        post.likes.add(request.user)
        liked = True  # flake8: noqa: F841

    return HttpResponseRedirect(reverse("blogs:post_detail", args=[str(post.slug)]))


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
    form_class = EditBlogForm
    success_url = reverse_lazy("blogs:show_all")


class DeleteBlogView(DeleteView):
    model = Post
    template_name = "blogs/delete_post.html"
    success_url = reverse_lazy("blogs:show_all")


class PostDetailView(DetailView):
    model = Post
    template_name = "blogs/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["slug"]

        # Comment form context data
        comment_form = CommentForm()
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True)

        # Likes context data
        blog_id = get_object_or_404(Post, slug=slug)
        total_likes = blog_id.total_likes()

        liked = bool(blog_id.likes.filter(id=self.request.user.id).exists())

        context["post"] = post
        context["comments"] = comments
        context["comment_form"] = comment_form
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=request.POST)
        self.object = self.get_object()
        slug = self.kwargs["slug"]
        # context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True)
        new_comment = None

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
            self.template_name,
            {"post": post, "comments": comments, "new_comment": new_comment, "comment_form": comment_form},
        )
