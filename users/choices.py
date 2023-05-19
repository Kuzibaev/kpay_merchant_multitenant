from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices


class UserType(TextChoices):
    SUPER_USER = 'super_user', _("super_user")
    COSTUMER = 'costumer', _("costumer")
