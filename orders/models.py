from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django_enumfield import enum

from buyers.models import Buyer, BankCard
from merchants.models import Merchant
from products.models import Product
from utility.models import BaseModel
from utility.enums import StatusEnum


class Order(BaseModel):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='merchant')
    buyer = models.ForeignKey(Buyer, on_delete=models.RESTRICT, related_name='buyer_order')
    bought_date = models.DateTimeField(_("bought date"), blank=True, null=True)
    interval = models.IntegerField(_("interval"))
    end_date = models.DateTimeField(_("end date"), blank=True, null=True)
    payment_date = models.IntegerField(_("payment date"), validators=[MinValueValidator(1), MaxValueValidator(31)])
    total_price = models.DecimalField(_("total price"), max_digits=20, decimal_places=2)
    first_payment = models.DecimalField(_("first payment"), max_digits=20, decimal_places=2)
    left_payment = models.DecimalField(_("left payment"), max_digits=20, decimal_places=2)
    status = enum.EnumField(StatusEnum, default=StatusEnum.OPENED)

    def __str__(self):
        return self.status


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    order_by = models.IntegerField(_("order by"))
    date = models.DateTimeField(_("date"))
    monthly_payment = models.DecimalField(_("monthly payment"), max_digits=20, decimal_places=2)
    remained_payment = models.DecimalField(_("remained payment"), max_digits=20, decimal_places=2)


class OrderProduct(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='products')
    serial_number = models.CharField(_("serial number"), max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField(_("quantity"))


class Payment(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='payment')
    amount = models.DecimalField(_("amount"), max_digits=20, decimal_places=2)
    bank_card = models.ForeignKey(BankCard, on_delete=models.RESTRICT, related_name='payment_bank_card')

    def __str__(self):
        return f"{self.amount} {self.bank_card.card_number}"
