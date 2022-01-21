# Generated by Django 3.2.10 on 2021-12-20 11:28

from django.db import migrations

import gnosis.eth.django.models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0052_keccak256_field_20211209_1628"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webhook",
            name="address",
            field=gnosis.eth.django.models.EthereumAddressV2Field(
                blank=True, db_index=True, null=True
            ),
        ),
    ]
