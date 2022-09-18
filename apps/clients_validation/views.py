from django.urls import reverse_lazy
from django.views import generic

from apps.clients_validation.forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    template_name = "clients/signup.html"
    success_url = reverse_lazy("login")
    form_class = CustomUserCreationForm
