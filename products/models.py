from django.db import models
from django.utils.translation import gettext_lazy as _

from images.models import Image
from merchants.models import Merchant
from utility.models import BaseModel


class Category(BaseModel):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(_("name"), max_length=100)
    description = models.CharField(_("description"), max_length=255)

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Product(BaseModel):
    serial_number = models.CharField(_("serial number"), max_length=255, null=False, blank=False)
    name = models.CharField(_("name"), max_length=255, null=False, blank=False)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='product_merchant')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_product')
    company = models.CharField(_("company"), max_length=128)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='product_images')
    model = models.CharField(_("model"), max_length=255)
    iclg = models.CharField(_("iclg"), max_length=128)
    color = models.CharField(_("color"), max_length=128)
    country = models.CharField(_("country"), max_length=128)
    price = models.DecimalField(_("price"), max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
