# Generated by Django 4.2 on 2023-05-14 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_cards', '0004_alter_bankcard_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankcard',
            name='card_number',
            field=models.CharField(max_length=255, verbose_name='card number'),
        ),
    ]
