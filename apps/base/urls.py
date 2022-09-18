from django.urls import path

from apps.base.views import HomeView

urlpatterns = [path("", HomeView.as_view(), name="index")]
