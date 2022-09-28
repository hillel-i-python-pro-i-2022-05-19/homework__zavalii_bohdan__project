from django.contrib.auth.decorators import login_required

from . import views
from django.urls import path

app_name = "blogs"

urlpatterns = [
    path("", views.PostList.as_view(), name="show_all"),
    # path("<slug:slug>/", login_required(views.PostDetail.as_view()), name="post_detail"),
    path("<slug:slug>/", login_required(views.post_detail), name="post_detail"),
]
