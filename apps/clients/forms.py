from django import forms

from apps.clients.models import Client


class ContactForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ("client_name", "is_live_account", "account_number")
