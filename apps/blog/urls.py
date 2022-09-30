from django.contrib.auth.decorators import login_required

from . import views
from django.urls import path, include

from .views import AddBlogView

app_name = "blogs"

urlpatterns = [
    path("", views.PostList.as_view(), name="show_all"),
    path("<slug:slug>/", login_required(views.post_detail), name="post_detail"),
    path("create", login_required(AddBlogView.as_view()), name="add_blog"),
    path(
        "<int:pk>/",
        include(
            [
                path("edit", login_required(views.UpdateBlogView.as_view()), name="edit"),
                path("delete", login_required(views.DeleteBlogView.as_view()), name="delete"),
            ]
        ),
    ),
]
