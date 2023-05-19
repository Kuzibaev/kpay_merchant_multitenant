from django.db import models
from django.utils.translation import gettext_lazy as _

from utility.models import BaseModel


class BankCard(BaseModel):
    card_number = models.CharField(_("card number"), max_length=255, null=False)
    expiry_month = models.CharField(_("expiry month"), max_length=2)
    expiry_year = models.CharField(_("expiry year"), max_length=2)
    is_verified = models.BooleanField(_("is_verified"), default=False)
