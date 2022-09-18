from django.urls import path

from apps.clients_validation import views

app_name = "clients"

urlpatterns = [
    path("", views.SignUpView.as_view(), name="signup"),
]
