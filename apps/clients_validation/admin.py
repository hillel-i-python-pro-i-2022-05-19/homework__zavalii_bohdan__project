from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AbstractClient

admin.site.register(AbstractClient, UserAdmin)
