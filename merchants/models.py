from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from utility.models import BaseModel


class Merchant(BaseModel):
    type = models.CharField(_("type"), max_length=100)
    name = models.CharField(_("name"), max_length=255)
    phone = PhoneNumberField(_("phone"))
    address = models.CharField(_("address"), max_length=255)
    bank_name = models.CharField(_("bank name"), max_length=150)
    mfo = models.IntegerField(_("mfo"))
    bank_account = models.CharField(_("bank account"), max_length=50)

    def __str__(self):
        return self.phone

    def __repr__(self):
        return self.phone
