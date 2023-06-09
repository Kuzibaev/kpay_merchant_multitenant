# Generated by Django 4.2 on 2023-04-18 08:44

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Buyer",
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
                    "pnfl",
                    models.CharField(max_length=14, unique=True, verbose_name="pnfl"),
                ),
                (
                    "first_name",
                    models.CharField(max_length=80, verbose_name="first name"),
                ),
                (
                    "middle_name",
                    models.CharField(blank=True, null=True, verbose_name="middle name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=80, verbose_name="last_name"),
                ),
                (
                    "passport_series",
                    models.CharField(max_length=10, verbose_name="passport series"),
                ),
                (
                    "passport_number",
                    models.CharField(max_length=10, verbose_name="passport number"),
                ),
                (
                    "passport_issued_by",
                    models.CharField(max_length=500, verbose_name="passport issued by"),
                ),
                (
                    "passport_date_of_issue",
                    models.DateField(verbose_name="passport date of issue"),
                ),
                (
                    "passport_date_of_expiry",
                    models.DateField(verbose_name="passport date of expiry"),
                ),
                ("birth_date", models.DateField(verbose_name="birth date")),
                ("limit", models.FloatField(default=10000000, verbose_name="limit")),
                (
                    "nationality",
                    models.CharField(max_length=100, verbose_name="nationality"),
                ),
                (
                    "citizenship",
                    models.CharField(max_length=150, verbose_name="citizenship"),
                ),
            ],
            options={
                "ordering": ("-id",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PhoneNumber",
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
                ("name", models.CharField(max_length=100, verbose_name="name")),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128,
                        region=None,
                        unique=True,
                        verbose_name="phone number",
                    ),
                ),
                ("is_main", models.BooleanField(default=False, verbose_name="is main")),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="buyer_phone_number",
                        to="buyers.buyer",
                    ),
                ),
            ],
            options={
                "ordering": ("-id",),
                "abstract": False,
            },
        ),
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
                    models.CharField(unique=True, verbose_name="card number"
                    ),
                ),
                ("expiry_month", models.CharField(verbose_name="expiry month")),
                ("expiry_year", models.CharField(verbose_name="expiry year")),
                ("is_main", models.BooleanField(default=True, verbose_name="is main")),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="buyer_card",
                        to="buyers.buyer",
                    ),
                ),
            ],
            options={
                "ordering": ("-id",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Address",
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
                ("name", models.CharField(max_length=100, verbose_name="name")),
                ("address", models.CharField(max_length=255, verbose_name="address")),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="buyer_address",
                        to="buyers.buyer",
                    ),
                ),
            ],
            options={
                "ordering": ("-id",),
                "abstract": False,
            },
        ),
    ]
