# Generated by Django 4.2 on 2023-04-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("credit_cards", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bankcard",
            name="card_number",
            field=models.CharField(unique=True, verbose_name="card number"),
        ),
    ]
