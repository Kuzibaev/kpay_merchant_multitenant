# Generated by Django 4.2 on 2023-04-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BankCard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="is deleted"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "card_number",
                    models.CharField(verbose_name="card number"
                                     ),
                ),
                (
                    "expiry_month",
                    models.CharField(max_length=2, verbose_name="expiry month"),
                ),
                (
                    "expiry_year",
                    models.CharField(max_length=2, verbose_name="expiry year"),
                ),
                (
                    "is_verified",
                    models.BooleanField(default=False, verbose_name="is_verified"),
                ),
            ],
            options={
                "ordering": ("-id",),
                "abstract": False,
            },
        ),
    ]
