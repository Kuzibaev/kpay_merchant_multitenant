# Generated by Django 4.2 on 2023-04-28 11:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0004_remove_image_is_deleted"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="image",
            options={
                "ordering": ("-id",),
                "verbose_name": "images",
                "verbose_name_plural": "images",
            },
        ),
    ]