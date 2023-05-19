from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from utility.models import BaseModel


class Buyer(BaseModel):
    pnfl = models.CharField(_("pnfl"), max_length=14, unique=True, null=False)
    first_name = models.CharField(_("first name"), max_length=80)
    middle_name = models.CharField(_("middle name"), max_length=80, null=True, blank=True)
    last_name = models.CharField(_("last_name"), max_length=80)
    passport_series = models.CharField(_("passport series"), max_length=10)
    passport_number = models.CharField(_("passport number"), max_length=10)
    passport_issued_by = models.CharField(_("passport issued by"), max_length=500)
    passport_date_of_issue = models.DateField(_("passport date of issue"))
    passport_date_of_expiry = models.DateField(_("passport date of expiry"))
    birth_date = models.DateField(_("birth date"))
    limit = models.FloatField(_("limit"), default=10000000)
    nationality = models.CharField(_("nationality"), max_length=100)
    citizenship = models.CharField(_("citizenship"), max_length=150)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return str(self.id)


class Address(BaseModel):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='addresses')
    name = models.CharField(_("name"), max_length=100)
    address = models.CharField(_("address"), max_length=255)

    def __str__(self):
        return self.name


class PhoneNumber(BaseModel):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='phone_numbers')
    name = models.CharField(_("name"), max_length=100)
    phone_number = PhoneNumberField(_("phone number"), null=False, blank=False)
    is_main = models.BooleanField(_("is main"), default=False, null=False)

    def __str__(self):
        return self.name


class BankCard(BaseModel):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='bank_cards')
    card_number = models.CharField(_("card number"), max_length=255, blank=False, null=False)
    expiry_month = models.CharField(_("expiry month"), max_length=255, null=False, blank=False)
    expiry_year = models.CharField(_("expiry year"), max_length=255, null=False, blank=False)
    is_main = models.BooleanField(_("is main"), default=True)

    def __str__(self):
        return self.card_number
