# Generated by Django 3.2.9 on 2021-11-29 11:11

import django.utils.timezone
from django.db import migrations, models

import gnosis.eth.django.models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0048_block_number_token_transfers_20211126_1443"),
    ]

    operations = [
        migrations.AddField(
            model_name="internaltx",
            name="block_number",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="internaltx",
            name="timestamp",
            field=models.DateTimeField(
                db_index=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="internaltx",
            name="_from",
            field=gnosis.eth.django.models.EthereumAddressField(null=True),
        ),
        migrations.AlterField(
            model_name="internaltx",
            name="to",
            field=gnosis.eth.django.models.EthereumAddressField(null=True),
        ),
        migrations.AddIndex(
            model_name="internaltx",
            index=models.Index(
                condition=models.Q(("value__gt", 0)),
                fields=["value"],
                name="history_internaltx_value_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="internaltx",
            index=models.Index(
                fields=["_from", "timestamp"], name="history_int__from_31d634_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="internaltx",
            index=models.Index(
                fields=["to", "timestamp"], name="history_int_to_e72886_idx"
            ),
        ),
        migrations.RunSQL(
            """
            UPDATE "history_internaltx" SET (block_number, timestamp) =
            (
                SELECT "history_ethereumblock"."number", "history_ethereumblock"."timestamp"
                FROM "history_ethereumtx" INNER JOIN "history_ethereumblock" ON (
                    "history_ethereumtx"."block_id" = "history_ethereumblock"."number"
                ) WHERE "history_internaltx"."ethereum_tx_id" = "history_ethereumtx"."tx_hash");
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
