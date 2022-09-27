from django.views.generic import ListView

from apps.clients.models import Client


class AboutUsView(ListView):
    model = Client
    template_name = "clients_show/about_us.html"
    context_object_name = "clients"
