from django.views.generic import ListView

from apps.clients.models import Client


class ShowAllClientsView(ListView):
    model = Client
    template_name = "clients_show/show_all.html"
    context_object_name = "clients"
