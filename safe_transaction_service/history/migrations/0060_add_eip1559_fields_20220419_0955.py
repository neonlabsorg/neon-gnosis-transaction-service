# Generated by Django 3.2.12 on 2022-04-19 09:55

from django.db import migrations, models

import gnosis.eth.django.models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0059_auto_20220408_1020"),
    ]

    operations = [
        migrations.AddField(
            model_name="ethereumtx",
            name="max_fee_per_gas",
            field=gnosis.eth.django.models.Uint256Field(
                blank=True, default=None, null=True
            ),
        ),
        migrations.AddField(
            model_name="ethereumtx",
            name="max_priority_fee_per_gas",
            field=gnosis.eth.django.models.Uint256Field(
                blank=True, default=None, null=True
            ),
        ),
        migrations.AddField(
            model_name="ethereumtx",
            name="type",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
