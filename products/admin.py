from django.contrib import admin

from products import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id',)
