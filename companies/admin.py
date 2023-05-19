from django.contrib import admin

from companies import models


@admin.register(models.CompanyName)
class CompanyNameAdmin(admin.ModelAdmin):
    list_display = ('id',)
