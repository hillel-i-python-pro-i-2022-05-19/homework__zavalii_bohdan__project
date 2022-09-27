from django.contrib.auth.decorators import login_required
from django.urls import path, include

from apps.clients import views

app_name = "clients_show"

urlpatterns = [
    path("", login_required(views.ShowAllClientsView.as_view()), name="show_all"),
    path("create", login_required(views.ClientCreateView.as_view()), name="create"),
    path(
        "<int:pk>/",
        include(
            [
                path("edit", login_required(views.ClientUpdateView.as_view()), name="edit"),
            ]
        ),
    ),
    path("about_us", login_required(views.AboutUsView.as_view()), name="about_us"),
]
