from django.db import models


class Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using('default')


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    objects = Manager()
