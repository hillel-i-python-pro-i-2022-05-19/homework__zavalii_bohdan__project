from . import views
from django.urls import path

app_name = "blogs"

urlpatterns = [
    path("", views.PostList.as_view(), name="show_all"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
