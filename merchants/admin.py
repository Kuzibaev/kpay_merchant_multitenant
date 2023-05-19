from django.contrib import admin

from merchants import models


@admin.register(models.Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ('id',)
