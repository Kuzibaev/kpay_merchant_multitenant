# Generated by Django 4.2 on 2023-04-26 12:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="is_deleted",
        ),
        migrations.RemoveField(
            model_name="product",
            name="is_deleted",
        ),
    ]
