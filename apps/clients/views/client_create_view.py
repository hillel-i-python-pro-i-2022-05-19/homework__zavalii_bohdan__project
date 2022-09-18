from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.clients.models import Client


class ClientCreateView(CreateView):
    model = Client
    fields = ["client_name", "is_live_account", "account_number"]
    success_url = reverse_lazy("clients_show:show_all")
