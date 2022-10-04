from django.db import models
from django.urls import reverse
from apps.clients_validation.models import AbstractClient
from ckeditor.fields import RichTextField

STATUS = ((0, "Draft"), (1, "Publish"))


class PostCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("index")

    __repr__ = __str__


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(AbstractClient, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    snippet = models.CharField(max_length=220)

    # If default=1, then all posts will be immediately displayed on the page,
    # but if default=0, then admin should go to admin panel and approve it manually.
    status = models.IntegerField(choices=STATUS, default=1)
    blog_category = models.CharField(max_length=200, default="uncategorized")

    likes = models.ManyToManyField(AbstractClient, related_name="blog_post_likes")

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
