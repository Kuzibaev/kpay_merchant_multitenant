from django.contrib import admin

from buyers import models


@admin.register(models.Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(models.Address)
class BuyerAddressAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(models.PhoneNumber)
class BuyerPhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(models.BankCard)
class BuyerBankCardAdmin(admin.ModelAdmin):
    list_display = ('id',)
