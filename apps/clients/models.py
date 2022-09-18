from django.db import models


class ClientDetail(models.Model):
    email_address = models.EmailField(
        "Email",
        max_length=254,
        help_text="It is the email address of the person",
        default="example@gmail.com",
        blank=True,
    )
    telegram_nickname = models.CharField("Telegram", max_length=100, help_text="Here is client's telegram", blank=True)
    linkedin_profile = models.CharField(
        "LinkedIn", max_length=500, help_text="Here is the link to contact's LinkedIn profile", blank=True
    )

    def __str__(self) -> str:
        return f"{self.email_address} - {self.telegram_nickname}," f"- {self.linkedin_profile} "

    __repr__ = __str__


class Client(models.Model):
    client_name = models.CharField("Client's name", max_length=200, help_text="It's the name of the client")
    is_live_account = models.CharField(
        "Live or Demo account", max_length=200, help_text="Shows whether the added account is live or demo"
    )

    account_number = models.CharField("IB's account number", max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.client_name} - {self.is_live_account} - {self.account_number}"

    __repr__ = __str__
