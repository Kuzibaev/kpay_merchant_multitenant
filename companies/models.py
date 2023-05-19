from django.db import models
from django.utils.translation import gettext_lazy as _

from utility.models import BaseModel


class CompanyName(BaseModel):
    full_name = models.CharField(_("full name"), max_length=255)
    address = models.CharField(_("address"), max_length=500)
    company_name = models.CharField(_("company name"), max_length=150)
    inn = models.CharField(_("inn"), max_length=50)
    bank_name = models.CharField(_("bank name"), max_length=255, null=False)
    bank_account = models.CharField(_("bank account"), max_length=50, null=False)
    mfo = models.CharField(_("mfo"), max_length=20, null=False)

    def __str__(self):
        return f'CompanyName {self.id}'

    def __repr__(self):
        return self.__str__()
