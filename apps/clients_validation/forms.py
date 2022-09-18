from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    error_css_class = "error-field"
    required_css_class = "required-field"
    password = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Password"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your username"}))

    class Meta(UserCreationForm.Meta):
        model = User
