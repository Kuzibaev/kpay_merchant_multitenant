from django.db import models

from django.utils.translation import gettext_lazy as _

from users.models import Customer
from utility.models import BaseModel


class Settings(BaseModel):
    user = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name='settings'
    )
    full_name = models.CharField(_("full name"), max_length=150)
    address = models.CharField(_("address"), max_length=255, null=False)
    company_name = models.CharField(_("company name"), max_length=150)
    inn = models.CharField(_("inn"), max_length=50, null=False, blank=False)
    bank_name = models.CharField(_("bank name"), max_length=150, null=False, blank=False)
    bank_account = models.CharField(_("bank account"), max_length=50, null=False, blank=False)
    mfo = models.IntegerField(_("mfo"))

    def __str__(self):
        return f"{self.company_name} : {self.full_name}"

    def __repr__(self):
        return self.__str__()
