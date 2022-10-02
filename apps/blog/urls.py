from django.contrib.auth.decorators import login_required

from . import views
from django.urls import path, include

from .views import AddBlogView
from .categories_views.add_category import AddCategoryView
from apps.blog.categories_views.category_veiw import category_view

app_name = "blogs"

urlpatterns = [
    path("", views.PostList.as_view(), name="show_all"),
    path("<slug:slug>/", login_required(views.post_detail), name="post_detail"),
    path("create", login_required(AddBlogView.as_view()), name="add_blog"),
    path("create_category", login_required(AddCategoryView.as_view()), name="add_category"),
    path("category/<str:cats>/", login_required(category_view), name="category"),
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
