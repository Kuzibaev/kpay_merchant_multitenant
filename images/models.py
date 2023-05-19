from django.db import models

from utility.models import BaseModel


class Image(BaseModel):
    image = models.ImageField(upload_to="images/%Y/%m/%d/")

    class Meta:
        verbose_name = 'images'
        verbose_name_plural = 'images'
        ordering = ('-id',)
