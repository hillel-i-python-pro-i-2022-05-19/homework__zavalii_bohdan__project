from django.contrib import admin
from apps.clients.models import Client, ClientDetail
from django.utils.html import format_html


class ClientAdmin(admin.ModelAdmin):
    list_display = ("client_name", "is_live_account", "account_number", "modified_at")


class ClientDetailAdmin(admin.ModelAdmin):
    list_display = ("email_address", "telegram_nickname", "contact_linkedin_profile")

    def contact_linkedin_profile(self, obj) -> format_html:
        return format_html(
            f"<a href='https://www.linkedin.com/in/{obj.linkedin_profile}' "
            f"target='_blank'>"
            f"{obj.linkedin_profile}</a>"
        )


admin.site.register(Client, ClientAdmin)
admin.site.register(ClientDetail, ClientDetailAdmin)
